import jsons
from entity.linklayer import Config


cfg = Config()
print(jsons.dumps(cfg.__dict__))