from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_username: str
    db_password: str
    db_host: str
    db_name: str
    db_port: int
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
