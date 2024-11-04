from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
class settings_dash(BaseSettings):
    admin_name:str
    admin_password:str
    jwt_secret:str

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_settings() -> settings_dash:
    return settings_dash()
