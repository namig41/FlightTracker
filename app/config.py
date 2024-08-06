from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    MODE: Literal["DEV", "TEST", "PROD"]

    DB_USER: str
    DB_PASSWORD: str
    DB_SERVER: str
    DB_PORT: str
    DB_NAME: str

    TEST_DB_USER: str
    TEST_DB_PASSWORD: str
    TEST_DB_SERVER: str
    TEST_DB_PORT: str
    TEST_DB_NAME: str

    SECRET_KEY: str
    ALGORITHM: str

    SMTP_HOST: str
    SMTP_PORT: str
    SMTP_USER: str
    SMTP_PASS: str

    class Config:
        env_file = ".env"


settings = Settings()
