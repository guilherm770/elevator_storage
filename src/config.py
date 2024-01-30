from pydantic_settings import BaseSettings
from functools import lru_cache
import os

from dotenv import load_dotenv
load_dotenv('.env')


class BaseConfig(BaseSettings):
    TZ: str

    class Config:
        env_file = ".env"        

class TestingConfig(BaseConfig):
    pass

class DevelopmentConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    pass

@lru_cache()
def get_settings():
    config_cls_dict = {
        "testing": TestingConfig,
        "development": DevelopmentConfig,
        "production": ProductionConfig
    }

    config_name = os.getenv("FASTAPI_CONFIG")
    config_cls = config_cls_dict[config_name]
    return config_cls()

settings = get_settings()