from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env',
                                      env_file_encoding='utf-8')
    db_type: str | None
    db_user: str | None
    db_password: str | None
    db_host: str | None
    db_port: int | None
    db_name: str | None
    db_ssl: str | None
    broker_url: str | None
    celery_backend_url: str | None
    celery_broker_url: str | None
    celery_result_backend: str | None


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
