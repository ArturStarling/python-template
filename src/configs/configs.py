from os.path import join, dirname, realpath

from pydantic import BaseSettings, SecretStr


class Configs(BaseSettings):
    API_KEY: SecretStr

    class Config:
        env_file = join(dirname(realpath(__file__)), ".env")
        env_file_encoding = "utf-8"
        case_sensitive = True


configs = Configs()
