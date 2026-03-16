"""
Modulo de Base de Conhecimento com RAG (Retrieval-Augmented Generation).
"""

import os
import logging
from typing import List

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

logger = logging.getLogger(__name__)


class KnowledgeBase:
    """Gerencia a base de conhecimento vetorial."""

    def __init__(self, config):
        self.config = config
        self.embeddings = OpenAIEmbeddings(
            openai_api_key=config.openai_api_key,
            model=config.embedding_model
        )
        self.vector_store = None
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap,
            separators=["\n\n", "\n", ". ", " ", ""]
        )

    def load_documents(self) -> List:
        """Carrega documentos da pasta docs/."""
        docs_path = self.config.docs_path
        if not os.path.exists(docs_path):
            logger.warning(f"Pasta {docs_path} nao encontrada. Criando...")
            os.makedirs(docs_path)
            return []

        loader = DirectoryLoader(
            docs_path,
            glob="**/*.txt",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"}
        )
        documents = loader.load()
        logger.info(f"Carregados {len(documents)} documentos.")
        return documents

    def build_vector_store(self):
        """Constroi o vector store a partir dos documentos."""
        documents = self.load_documents()
        if not documents:
            logger.warning("Nenhum documento encontrado.")
            return

        chunks = self.text_splitter.split_documents(documents)
        logger.info(f"Criados {len(chunks)} chunks.")

        self.vector_store = FAISS.from_documents(chunks, self.embeddings)
        logger.info("Vector store criado com sucesso.")

    def search(self, query: str, k: int = 3) -> str:
        """Busca documentos relevantes na base."""
        if not self.vector_store:
            return "Base de conhecimento nao inicializada."

        docs = self.vector_store.similarity_search(query, k=k)
        context = "\n\n".join([doc.page_content for doc in docs])
        return context
