from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Job Agent"
    ollama_model: str = "qwen3:8b"
    ollama_base_url: str = "http://localhost:11434"

    class Config:
        env_file = ".env"


settings = Settings()