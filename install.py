import argparse
import sys
import os
import hashlib
import bcrypt

description = "Simple installer dashboard web for linklayer"
parser = argparse.ArgumentParser(description=description)
parser.add_argument("--port",help="Port for webdashboard")
parser.add_argument("--host",help="Host ip for listen dashboard web")
parser.add_argument("--username",help="Username for login dashboard")
parser.add_argument("--password",help="Password for login dashboard")

args = parser.parse_args()

if not args.host or not args.port or not args.username or not args.password:
    print("Expected other params")
    sys.exit(1)



if not os.getuid() == 0:
    print("Run this script as root!!!!")
    sys.exit(1)

if os.path.exists(".env"):
    print("Error delete .env file")
    sys.exit(1)

print("Cloning repository")

os.system("git clone https://iopmx@bitbucket.org/iopmx/linklayer-vpn-server.git")
os.system("mv linklayer-vpn-server binary")
os.system("rm binary/cfg/config.json")


print("Craete env file")
f_env = open(".env","w")
f_env.write("ADMIN_NAME=\""+args.username+"\"\n")

bytes = args.password.encode('utf-8') 
salt = bcrypt.gensalt() 
hash = bcrypt.hashpw(bytes, salt) 
hashed = hash.decode("utf-8")
f_env.write("ADMIN_PASSWORD=\""+hashed+"\"\n")
jwt_hash = hashlib.md5(hashed.encode())
f_env.write("JWT_SECRET=\""+jwt_hash.hexdigest()+"\"\n")
f_env.close()

print("Creating service and start")
working = sys.argv[0]
working_dir = os.path.dirname(os.path.abspath(working))
working_dir = working_dir.replace(" ","\\ ",-1)
service ="""[Unit]
Description=Linklayer-Dashboard
Wants=network-online.target
After=network.target network-online.target

[Service]
CapabilityBoundingSet=CAP_NET_BIND_SERVICE CAP_NET_ADMIN
AmbientCapabilities=CAP_NET_BIND_SERVICE CAP_NET_ADMIN
User=root
Type=simple
TimeoutStopSec=1
LimitNOFILE=infinity
WorkingDirectory={}
ExecStart={}

[Install]
WantedBy=multi-user.target""".format(working_dir,working_dir+"/dashweb/bin/uvicorn main:app --host {} --port {}".format(args.host,args.port))

f_service = open("/etc/systemd/system/dashlink.service","w")
f_service.write(service)
f_service.close()
os.system("systemctl daemon-reload")
os.system("systemctl enable dashlink.service")
os.system("systemctl start dashlink.service")
print("Sucess you can acces from your web browser http://{}:{}".format(args.host,args.port))
