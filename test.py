import jsons
from entity.linklayer import HTTP, HTTPTLS, TLS, TLS1, Config, HTTPResponse, Service


cfg = Config()
service = Service()
httptls = HTTPTLS()
http = HTTPResponse()

http.Response = "HTTP/1.1 200 OK\r\n\r\n"
tls = TLS1
tls.Key = "/opt/fladsf"
tls.Cert = "/opt/flafd"


httptls.Http = http
httptls.TLS = tls
httptls.Listen = "0.0.0.0:440"
service.type = "httptls"
service.cfg = httptls

cfg.services.append(service)
print(jsons.dumps(cfg.__dict__))