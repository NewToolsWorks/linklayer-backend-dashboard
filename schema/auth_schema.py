from dataclasses import dataclass
from pydantic import BaseModel


class request_signing(BaseModel):
    username:str
    password:str

@dataclass
class jwt_data:
    csrf:str = ""
    username:str = ""
    ip:str = ""
    #More data will be saved later if you have any suggestions, they are welcome.