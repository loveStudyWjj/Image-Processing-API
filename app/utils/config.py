from pydantic_settings  import BaseSettings

class Settings(BaseSettings):
    mysql_host: str = ""
    mysql_user: str = ""
    mysql_password: str = ""
    mysql_db: str = ""
    redis_host: str = ""
    redis_port: int = 0
    redis_db: int = 0

    class Config:
        env_file = ".env"

settings = Settings()




