import jsons
from entity.linklayer import HTTP, HTTPTLS, TLS, Config, Service


cfg = Config()
service = Service()
httptls = HTTPTLS()
http = HTTP()
http.Listen = "0.0.0.0:80"
http.Response = "HTTP/1.1 200 OK\r\n\r\n"
tls = TLS()
tls.Key = "/opt/fladsf"
tls.Cert = "/opt/flafd"
tls.Listen = "0.0.0.0:443"

httptls.Http = http
httptls.TLS = tls

service.type = "httptls"
service.cfg = httptls

cfg.services.append(service)
print(jsons.dumps(cfg.__dict__))