from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = 'sqlite+aiosqlite:///thankme.db'
    db_echo: bool = True


settings = Settings()
