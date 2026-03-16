"""
Logica do Agente de IA - Assistente Virtual com RAG.
"""

import logging
import time
from typing import List, Dict

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from config import Config
from knowledge_base import KnowledgeBase
from prompts import SYSTEM_PROMPT, QA_PROMPT

logger = logging.getLogger(__name__)


class AIAgent:
    """Agente de IA com RAG para respostas contextualizadas."""

    def __init__(self, config: Config):
        self.config = config
        self.llm = ChatOpenAI(
            openai_api_key=config.openai_api_key,
            model_name=config.model_name,
            temperature=config.temperature,
            max_tokens=config.max_tokens
        )
        self.kb = KnowledgeBase(config)
        self.conversation_history: List[Dict] = []
        self.metrics = {"queries": 0, "avg_time": 0, "total_time": 0}

    def initialize(self):
        """Inicializa a base de conhecimento."""
        logger.info("Inicializando base de conhecimento...")
        self.kb.build_vector_store()
        logger.info("Agente pronto.")

    def ask(self, question: str) -> str:
        """Processa uma pergunta e retorna resposta contextualizada."""
        start_time = time.time()

        try:
            # Buscar contexto relevante
            context = self.kb.search(question)

            # Montar prompt com contexto
            prompt = ChatPromptTemplate.from_template(QA_PROMPT)
            chain = prompt | self.llm

            response = chain.invoke({
                "context": context,
                "question": question
            })

            answer = response.content.strip()

            # Atualizar historico
            self.conversation_history.append({
                "role": "user", "content": question
            })
            self.conversation_history.append({
                "role": "assistant", "content": answer
            })

            # Metricas
            elapsed = time.time() - start_time
            self.metrics["queries"] += 1
            self.metrics["total_time"] += elapsed
            self.metrics["avg_time"] = (
                self.metrics["total_time"] / self.metrics["queries"]
            )

            logger.info(f"Resposta gerada em {elapsed:.2f}s")
            return answer

        except Exception as e:
            logger.error(f"Erro ao processar pergunta: {e}")
            return f"Desculpe, ocorreu um erro: {e}"

    def get_metrics(self) -> Dict:
        """Retorna metricas de desempenho."""
        return self.metrics

    def clear_history(self):
        """Limpa o historico de conversas."""
        self.conversation_history = []
