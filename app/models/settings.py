from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    mongodb_dsn: str
    db_name: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'