from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Class for storing settings."""
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    RABBITMQ_LOGIN: str
    RABBITMQ_PASSWORD: str
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')    

    @property
    def amqp_url(self):
        return f"amqp://{self.RABBITMQ_LOGIN}:{self.RABBITMQ_PASSWORD}@{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}/"
    
    
settings = Settings()