import jsons
from entity.linklayer import Config


cfg = Config()
jsons.dumps(cfg.__dict__)