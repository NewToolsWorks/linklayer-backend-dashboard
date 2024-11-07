
from asyncio import sleep
from collections import namedtuple

from typing import Annotated
from fastapi import  Depends, FastAPI, HTTPException, Path, Request, Response, UploadFile, status
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from jwt import InvalidTokenError
from core.auth import Authentication

from core.conn import getConn
from core.settings import get_settings
from entity.linklayer import Auth, Config, Service
from entity.users import CreateUser, DeleteUser, ModifyUser
from core.users import createUser, deleteUser, modifyUser, readUsers
from schema.auth_schema import jwt_data, request_signing
import os
import sys
import json
import jsons
from datetime import date, timedelta,datetime
from schema.file_schema import file_arg
from schema.linklayer_schema import DNSTTParam, HTTPDualParam, HTTPParam, HTTPTLSParam, TLSParam, UDPParam
import subprocess
from core.utils import get_network_ip
from core.service.linklayer import LinkLayer
from core.service.linklayer_auth import Authenticator
from time import time
from anyio import open_file
import threading
import random
import glob
import urllib


def load_config()->Config:
    if os.path.exists("binary/cfg/config.json"):
        f = open("binary/cfg/config.json","r")
        all = f.read()
        js = jsons.loads(all)
        f.close()
        return Config(**js)
    else:
        cfg = Config()
        cfg.auth = "unix"
        cfg.path = "/var/run/lnk-handler.sock"
        return cfg

link_service = LinkLayer()
service_config = load_config()
app = FastAPI()
route = FastAPI()
auth = Authentication()




##### VIEWS
route.mount("/assets",StaticFiles(directory="public/assets"))
route.mount("/login/",StaticFiles(directory="public",html=True))

@route.get("/dashboard/{path:path}")
async def dashboard_sections(path:str):
    return FileResponse("public/index.html")

@route.get("/user-config")
async def user_config():
    return FileResponse("public/index.html")
#### VIEWS

app.mount("/",route)

async def require_logged(request:Request)->any:

    ipClient = request.client.host if  request.headers.get("x-forwarded-for") == None else request.headers.get("x-forwarded-for")
   
    token = request.cookies.get("token")
   
    if token == None or token == "":
     
        raise InvalidTokenError
    if not auth.verifyJWT(token):
  
        raise InvalidTokenError
    raw = auth.decodeJWT(token)
 
    user = jwt_data(**raw)
    if not user.ip == ipClient:
    
        raise InvalidTokenError
    
    return user

async def require_loggued_api(request:Request) -> any:
    
    csrf = request.query_params["csrf"]
    csrf_cookie = request.cookies.get("csrf")
  
    if not csrf == csrf_cookie:
        raise InvalidTokenError

    return await require_logged(request) 
   


@app.middleware("http")
async def session_handle(request: Request, call_next):
    path = request.url.path.lower()
    if path.startswith("/dashboard") or path.startswith("/user-config"):
        try:
            await require_logged(request)
            response = await call_next(request)
            return response
        except Exception as ex:
     
            return RedirectResponse("/login")
    if path.startswith("/login"):
        
        try:
            await require_logged(request)
         
            return RedirectResponse("/dashboard")
        except:
          
            pass    
    return await call_next(request)

def remove_by_type(type_layer:str):
    services_copy = service_config.services[:]
    for service in services_copy:
        if type(service) is dict:
            if service["type"] == type_layer:
                service_config.services.remove(service)
        else:    
            if service.type == type_layer:         
                service_config.services.remove(service)
       
def get_by_type(type_layer:str):
    result = []
   
    for service in service_config.services:
        if type(service) is dict:
            if service["type"] == type_layer:
                result.append(service["cfg"])    
        else:
            if service.type == type_layer:         
                result.append(service.cfg)
    return result



@route.post("/api/login")
async def login(AuthRequest:request_signing,request:Request,response:Response):
    token = request.cookies.get("token")
    ipClient = request.client.host if  request.headers.get("x-forwarded-for") == None else request.headers.get("x-forwarded-for")

    access_token = "" if token == None else token 
    if not auth.login(AuthRequest,access_token):
        return JSONResponse({"status":"error","message":"Cant login, check your creds"},status.HTTP_401_UNAUTHORIZED)
    
    token,csrf = auth.generateJWT(ipClient)
    response.set_cookie("token",token,httponly=True)
    response.set_cookie("csrf",csrf,httponly=True)
    abspath = os.path.abspath("binary")
    
    return {"csrf":csrf,"base":abspath}


@route.get("/api/get/auth")
async def get_authService(user:Annotated[any,Depends(require_loggued_api)]):
   
    return {"banner":service_config.banner,"limit_conn_request":service_config.limit_conn_request,"limit_conn_single":service_config.limit_conn_single}

@route.post("/api/auth")
async def authService(user:Annotated[any,Depends(require_loggued_api)],auth:Auth):
    
    service_config.banner = auth.banner
    service_config.limit_conn_request = auth.limit_conn_request
    service_config.limit_conn_single = auth.limit_conn_single

    return {"status":"ok"}



@route.post("/api/{action}/user")
async def manageUsers(action:str,user:Annotated[any,Depends(require_loggued_api)],request:Request):
   
    body = await request.body()
    raw = json.loads(body)
    
    if len(raw) == 0 and not action == "read":
          raise HTTPException(400,"Bad request")
    
    if action == "create":
     
        usercreate = CreateUser(**raw)
        expireTime = 0
        if not usercreate.expdisable and usercreate.expire == "":
            raise HTTPException(400,"Error expire time invalid")

        if not usercreate.expdisable and not usercreate.expire == "":
            dateExpire = date.fromisoformat(usercreate.expire)
            expirDT = datetime(dateExpire.year,dateExpire.month,dateExpire.day,0,0)
            epochDT = datetime(1970, 1, 1)
            delta = (expirDT - epochDT)
            expireTime = int(delta.total_seconds())

        if usercreate.username == "" or usercreate.password == "":
            raise HTTPException(400,"Invalid username or password")
      
       
        createUser(usercreate,expireTime)
        return {"status":"ok"}
    if action == "read":
        
        return readUsers()
    if action == "delete":
        userdelete = DeleteUser(**raw)
        deleteUser(userdelete.id)
        return {"status":"ok"}
    if action == "modify":
        usermodify = ModifyUser(**raw)
        expireTime = 0
        changePassword = not usermodify.password == ""
        if  not usermodify.expdisable and usermodify.expire == "":
            raise HTTPException(400,"invalid update expire")
        if not usermodify.expdisable and not usermodify.expire == "":
            dateExpire = date.fromisoformat(usermodify.expire)
            expirDT = datetime(dateExpire.year,dateExpire.month,dateExpire.day,0,0)
            epochDT = datetime(1970, 1, 1)
            delta = (expirDT - epochDT)
            expireTime = int(delta.total_seconds())
        modifyUser(usermodify,changePassword,expireTime)
        return {"status":"ok"}

@route.get("/api/read/{layer}")
async def readLayer(layer:str ,user:Annotated[any,Depends(require_loggued_api)]):
    if layer == "udp":
        ifs = get_network_ip()
        networks = []
        for ifs1 in ifs:
            networks.append({"NetName":ifs1[0],"Ip":ifs1[1]})
        return {"extra":{"networks":networks},"service":get_by_type(layer)}

    if layer == "dnstt":
        public_key =""
        if os.path.isfile("binary/layers/cfgs/dnstt-priv.key"):
            f = open("binary/layers/cfgs/dnstt-public.pub","r")
            public_key = f.read()
            f.close()
        else:
            subprocess.run(["./binary/layers/dnstt-server","-gen-key","-privkey-file","binary/layers/cfgs/dnstt-priv.key","-pubkey-file","binary/layers/cfgs/dnstt-public.pub"])
            f = open("binary/layers/cfgs/dnstt-public.pub","r")
            public_key = f.read()
            f.close()
        public_key = public_key.strip()    
        ifs = get_network_ip()
        networks = []
        for ifs1 in ifs:
            networks.append({"NetName":ifs1[0],"Ip":ifs1[1]})
      
        return {"extra":{"public":public_key,"networks":networks},"service": get_by_type(layer)}
    
    return get_by_type(layer)


@route.post("/api/layer/{layer}")
async def createLayer(layer:str ,user:Annotated[any,Depends(require_loggued_api)],req:Request):
      body  = await req.body()
      raw = json.loads(body)
      if len(raw) == 0:
          raise HTTPException(400,"Bad request")
      if layer == "http":
           
            http_param  = HTTPParam(**raw)
         
            if http_param.enabled:
                remove_by_type("http")
               
                for service in http_param.h:
                    servicehttp = Service()
                    servicehttp.type = "http"
                    servicehttp.cfg = service
                    service_config.services.append(servicehttp)
            else:            
                remove_by_type("http")
        
      if layer == "tls":
            
            tls_param  = TLSParam(**raw)
          
            if tls_param.enabled:
                remove_by_type("tls")
               
                for service in tls_param.t:
                    servicetls = Service()
                    servicetls.type = "tls"
                    servicetls.cfg = service
                    service_config.services.append(servicetls)
            else:            
                remove_by_type("tls")
            
      if layer == "httptls":
             httptls_param  = HTTPTLSParam(**raw)
         
             if httptls_param.enabled:
                remove_by_type("httptls")
               
                for service in httptls_param.ht:
                    servicehttptls = Service()
                    servicehttptls.type = "httptls"
                    servicehttptls.cfg = service
                    service_config.services.append(servicehttptls)
             else:            
                remove_by_type("httptls")  
      if layer == "dnstt":
          dnstt_param = DNSTTParam(**raw)
          if dnstt_param.enabled:
              remove_by_type("dnstt")
              servicednstt = Service()
              servicednstt.type = "dnstt"
              servicednstt.cfg = dnstt_param.d
              service_config.services.append(servicednstt)
          else:
              remove_by_type("dnstt")

      if layer == "udp":
          udp_param = UDPParam(**raw)
          if udp_param.enabled:
              remove_by_type("udp")
              serviceudp = Service()
              serviceudp.type = "udp"
              serviceudp.cfg = udp_param.u
              service_config.services.append(serviceudp)
          else:
              remove_by_type("udp")
          
      if layer == "httpdual":
          httpdual_param = HTTPDualParam(**raw)
          if httpdual_param.enabled:
              remove_by_type("httpdual")
              for service in httpdual_param.hd:
                    servicehttpdual = Service()
                    servicehttpdual.type = "httpdual"
                    servicehttpdual.cfg = service
                    service_config.services.append(servicehttpdual)   
          else:
             remove_by_type("httpdual")       
      
      return {"status":"ok"}
    

@route.get("/api/get_status_service")
async def get_status_service(user:Annotated[any,Depends(require_loggued_api)]):
    return {"status":link_service.get_service_status()}

@route.get("/api/start_service")
async def start_service(user:Annotated[any,Depends(require_loggued_api)]):
    if await link_service.start_service(service_config):
        return {"code":1,"message":"Service started sucessfully :D"}
    else:
        return {"code":0,"message":"Cant start service check logs for more information"}

@route.get("/api/stop_service")
async def stop_service(user:Annotated[any,Depends(require_loggued_api)]):
    link_service.stop_service()


@route.get("/api/logs")
async def read_logs(user:Annotated[any,Depends(require_loggued_api)]):
    
    f = await open_file("log.txt")
    result_log = []
    while True:
        line = await f.readline()
        line = line.strip()
        if line == "":
            break
        result_log.append(line)

    await f.aclose()   
    
    return result_log

@route.post("/api/cfg/upload")
async def upload_file(user:Annotated[any,Depends(require_loggued_api)],cfg: UploadFile):
    data  =await cfg.read()
    f = open("public/assets/"+cfg.filename,mode="wb")
    f.write(data)
    f.close()
    return {"result":"ok"}

@route.post("/api/cfg/delete")
async def delete_file(user:Annotated[any,Depends(require_loggued_api)],fdelete:file_arg):
    os.remove("public/assets/"+fdelete.filename)
    return {"result":"ok"}


@route.post("/api/cfg/setEnabled/{enabled}")
async def set_enabled(user:Annotated[any,Depends(require_loggued_api)],enabled:int):
    enable = enabled == 1

    conn = getConn()
    conn.execute("update cfgdash set remote = ?",(enable,))
    return {"result":"ok"}

@route.get("/public/announce")
def available_configs(req:Request):
    conn = getConn()
    enabled =conn.query("select remote from cfgdash").fetchall()
    if not enabled[0][0]:
        return {}
    Host = req.headers.get("Host")
    files = []
    for f in (glob.glob("public/assets/*.lnk")):
        f = os.path.basename(f)
        name = f.replace(".lnk","")
        f = urllib.parse.quote(f)
        url = "http://"+Host+"/assets/"+f
        files.append({"name":name,"url":url})

    videos = glob.glob("public/assets/*.mp4")
    video_url = ""
    if len(videos) >= 1:
        first_video = videos[0]
        first_video = os.path.basename(first_video)
        first_video = urllib.parse.quote(first_video)
        video_url = "http://"+Host+"/assets/"+first_video
    return {"cfgs":files,"video":video_url}

@route.post("/api/cfg/video")
async def get_files(user:Annotated[any,Depends(require_loggued_api)],video:UploadFile):
    content = await video.read()
    f = open("public/assets/video.mp4","wb")
    f.write(content)
    f.close()
    return {"status":"ok"}

@route.get("/api/cfg/delete/video")
async def get_files(user:Annotated[any,Depends(require_loggued_api)]):
    os.remove("public/assets/video.mp4")
    return {"status":"ok"}


@route.get("/api/cfg")
async def get_files(user:Annotated[any,Depends(require_loggued_api)],request:Request):
    host = request.headers.get("host")
    conn = getConn()
    enabled =conn.query("select remote from cfgdash").fetchall()
    
    files = glob.glob("public/assets/*.lnk")
    result = []
    for f in files:
        result.append(os.path.basename(f))

    videos = glob.glob("public/assets/*.mp4")
    video_url = ""
    if len(videos) >= 1:
        first_video = videos[0]
        first_video = os.path.basename(first_video)
        first_video = urllib.parse.quote(first_video)
        video_url = "http://"+host+"/assets/"+first_video 
    url = "http://"+host+"/public/announce"
    return {"enabled":enabled[0][0],"files":result,"announce":url,"video":video_url}


@route.get("/api/logout", response_class=HTMLResponse)
async def logout(user:Annotated[any,Depends(require_loggued_api)],response:Response):
    phrases = [
    "I will be ready for you when you return. Come back soon!",
    "This isn't goodbye, just a break. Hope to see you again!",
    "I would be glad to work with you again. See you soon!",
    "There will always be a place for you here. Return whenever you're ready!",
    "Until we meet again. See you soon!",
    "Don't take too long, I'll be ready to collaborate again.",
    "I hope you come back soon, your contribution will be greatly appreciated!",
    "Time flies, so come back when you're ready. Looking forward to it!",
    "Come back soon! The best opportunities are yet to come.",
    "Don't forget about me, see you soon!"  
    ]
    prhase = phrases[random.randrange(0,9)]
    response.delete_cookie("csrf")
    response.delete_cookie("token")
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Logout</title>
    <script>
        
        setTimeout(function() {
            window.location.href = "/login";
        }, 4500);
    </script>
</head>
<body>
    <h1>Redirect...</h1>
    <p>"""+prhase+"""</p>
</body>
</html>

    """


link_auth = Authenticator(service_config.path,getConn())
thread_auth = threading.Thread(target=link_auth.start_server)
thread_auth.start()
