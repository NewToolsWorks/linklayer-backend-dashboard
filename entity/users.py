
from dataclasses import dataclass


@dataclass
class CreateUser:
    username:str = ""
    password:str = ""
    expdisable:bool = False
    expire:str = ""

@dataclass
class ResultUser(CreateUser):
    id:int = 0


@dataclass
class DeleteUser():
    id:int = 0

@dataclass
class ModifyUser(CreateUser):
    id:int = 0
    