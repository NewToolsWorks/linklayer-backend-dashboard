import jwt
from core.settings import get_settings
from schema import auth_schema
import bcrypt
import uuid

class Authentication:
    def __init__(self) -> None:
         self.ALGORITHM = "HS256"
         self.settings = get_settings()
    def generateJWT(self,ipClient:str)->any:
 

        jwt_secret = self.settings.jwt_secret
        username = self.settings.admin_name
        data = auth_schema.jwt_data()
        data.csrf = str(uuid.uuid4())
        data.ip = ipClient
        data.username = username
        return  (jwt.encode(data.__dict__,jwt_secret,self.ALGORITHM),data.csrf)
    
    def decodeJWT(self,token:str) -> any:
        return jwt.decode(token,self.settings.jwt_secret,self.ALGORITHM)


    def verifyJWT(self,token:str) -> bool:
        
        decoded =  self.decodeJWT(token)
        if not decoded.get("username") == None:

            return True
        return False

    def isLoggedin(self,token:str)->bool:
        if not token == "" and self.verifyJWT(token):
            return True
        return False

    def login(self,auth:auth_schema,token:str) -> bool:
        if self.isLoggedin(token):
            return False
        

        settings = get_settings()
        
        if not auth.username  == settings.admin_name:
            return False
        
      
        passAuth = auth.password.encode("utf-8")
        hash = settings.admin_password.encode("utf-8")
        return bcrypt.checkpw(passAuth, hash)
            
        
