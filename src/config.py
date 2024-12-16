from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    1. First checks actual environment variables
    2. Then checks the .env file specified in Config
    3. Finally falls back to default values in the class
    """
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/bookdb"

    class Config:
        env_file = ".env"

settings = Settings()