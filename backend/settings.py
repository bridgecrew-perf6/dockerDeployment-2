from pydantic import BaseSettings
from dotenv import load_dotenv


class Settings(BaseSettings):
    ssh_key: str
    client_id: str
    tenant: str
    client_credential: str


load_dotenv()
settings = Settings()
