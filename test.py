import jsons
from entity.linklayer import HTTP, HTTPTLS, TLS, TLS1, Config, HTTPResponse, Service


cfg = Config()
service = Service()

http = HTTPResponse("HTTP/1.1 200 OK\r\n\r\n")

tls = TLS1( "/opt/fladsf", "/opt/fladsf")


httptls = HTTPTLS(http,tls,"0.0.0.0:443")
service.type = "httptls"
service.cfg = httptls

cfg.services.append(service)
print(jsons.dumps(cfg.__dict__))