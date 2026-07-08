"""
Configuration centrale de l'application.
Charge les variables d'environnement depuis le fichier .env
et les expose de manière typée via pydantic-settings.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- App ---
    app_name: str = "AO Radar"
    environment: str = "development"

    # --- BOAMP / data.gouv.fr ---
    boamp_api_base_url: str = "https://boamp-datadila.opendatasoft.com/api/records/1.0/search/"

    # --- LLM (à venir) ---
    groq_api_key: str = ""

    # --- Supabase (à venir) ---
    supabase_url: str = ""
    supabase_key: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
