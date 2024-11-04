
from dataclasses import dataclass, field

from entity.linklayer import DNSTT, HTTP, HTTPTLS, TLS, UDP, Auth, HTTPDual


@dataclass
class HTTPDualParam:
    enabled:bool = False
    hd:[HTTPDual] = field(default_factory=list)

@dataclass
class UDPParam:
    enabled:bool = False
    u:UDP = None

@dataclass
class DNSTTParam:
    enabled:bool = False
    d:DNSTT = None

@dataclass
class HTTPTLSParam:
    enabled:bool = False
    ht:[HTTPTLS] = field(default_factory=list)

@dataclass
class TLSParam:
    enabled:bool = False
    t:[TLS] = field(default_factory=list)


@dataclass
class HTTPParam:
    enabled:bool = False
    h:[HTTP] = field(default_factory=list) 

@dataclass
class AuthParam(Auth):
    pass