"""
Assistente Virtual com IA Generativa - Modo Terminal
Projeto Final DIO Bradesco GenAI & Dados
Autor: Gabriel Demetrios Lafis
"""

import sys
import logging
from dotenv import load_dotenv

from config import Config
from agent import AIAgent

logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()


def main():
    print("="*60)
    print("  DataBot - Assistente Virtual com IA Generativa")
    print("  Projeto Final DIO Bradesco GenAI & Dados")
    print("="*60)

    config = Config()
    if not config.openai_api_key:
        print("Erro: OPENAI_API_KEY nao configurada.")
        sys.exit(1)

    agent = AIAgent(config)
    agent.initialize()

    print("\nDigite suas perguntas ou 'sair' para encerrar.")
    print("Comandos: 'metricas' | 'limpar' | 'sair'")
    print("-"*60)

    while True:
        try:
            question = input("\nVoce: ").strip()
            if not question:
                continue
            if question.lower() in ['sair', 'exit', 'quit']:
                print("Ate mais!")
                break
            if question.lower() == 'metricas':
                m = agent.get_metrics()
                print(f"Consultas: {m['queries']} | Tempo medio: {m['avg_time']:.2f}s")
                continue
            if question.lower() == 'limpar':
                agent.clear_history()
                print("Historico limpo.")
                continue

            response = agent.ask(question)
            print(f"\nDataBot: {response}")

        except KeyboardInterrupt:
            print("\nAte mais!")
            break


if __name__ == "__main__":
    main()
