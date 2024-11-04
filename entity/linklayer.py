from dataclasses import dataclass, field
from typing import List, Optional

from pydantic import BaseModel

@dataclass
class HTTPDual:
    Key: str
    Cert: str
    Limit: str
    PacketBuffer: int
    IsTLS: bool
    Listen: str


@dataclass
class TLS1:
    Cert: str
    Key: str  

@dataclass
class TLS:
    Cert: str
    Key: str
    Listen: str

@dataclass
class HTTP:
    Response: str
    Listen: str

@dataclass
class HTTPResponse:
    Response: str

@dataclass
class HTTPTLS:
    Http: HTTPResponse
    TLS: TLS1
    Listen: str

@dataclass
class UDP:
    listen: str
    exclude: str
    net: str
    cert: str
    key: str
    obfs: str
    max_conn_client: int

@dataclass
class DNSTT:
    Domain: str
    Net: str

@dataclass
class Service:
    type: str = ""
    cfg: object   = None

@dataclass
class Auth:
    banner: str = ""
    limit_conn_single: int = -1
    limit_conn_request: int = -1

@dataclass
class Config(Auth):
    auth: str = "unix"
    path:str = "/tmp/linklayer-handle.sock"
    services: List[Service] = field(default_factory=list)