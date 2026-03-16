"""
Configuracao do Assistente Virtual com IA Generativa.
"""

import os
from dataclasses import dataclass


@dataclass
class Config:
    """Configuracoes do assistente virtual."""
    openai_api_key: str = None
    model_name: str = "gpt-3.5-turbo"
    embedding_model: str = "text-embedding-ada-002"
    temperature: float = 0.7
    max_tokens: int = 1000
    chunk_size: int = 500
    chunk_overlap: int = 50
    docs_path: str = "docs"
    vector_store_path: str = "vector_store"

    def __post_init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY", self.openai_api_key)
        self.model_name = os.getenv("MODEL_NAME", self.model_name)
        self.temperature = float(os.getenv("TEMPERATURE", self.temperature))
