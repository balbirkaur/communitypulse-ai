"""Configuration management for the application."""

from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    model_config = ConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore"
    )

    # Application
    app_name: str = "Community Pulse AI"
    app_version: str = "0.1.0"
    debug: bool = False

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    # Google Cloud
    gcp_project_id: Optional[str] = None
    gcp_location: str = "us-central1"

    # BigQuery
    bigquery_dataset: Optional[str] = None
    bigquery_table_prefix: str = "communitypulse_"

    # Vertex AI
    vertex_model_name: Optional[str] = None
    
    # Vector Search
    vector_search_enabled: bool = False
    vector_search_index: Optional[str] = None
