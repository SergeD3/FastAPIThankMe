from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = 'postgresql+asyncpg://postgres:Fo*vMTYdk8INcCO30hSb@localhost:5432/thankme'
    db_echo: bool = False


settings = Settings()
