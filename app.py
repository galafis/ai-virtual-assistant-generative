"""
Interface Streamlit - Assistente Virtual com IA Generativa
"""

import streamlit as st
from dotenv import load_dotenv

from config import Config
from agent import AIAgent

load_dotenv()

st.set_page_config(
    page_title="DataBot - Assistente IA",
    page_icon="🤖",
    layout="wide"
)


@st.cache_resource
def init_agent():
    config = Config()
    agent = AIAgent(config)
    agent.initialize()
    return agent


def main():
    st.title("🤖 DataBot - Assistente Virtual com IA Generativa")
    st.markdown("*Projeto Final DIO Bradesco GenAI & Dados*")
    st.divider()

    # Sidebar
    with st.sidebar:
        st.header("Sobre")
        st.markdown(
            "Assistente especialista em **Data Science**, "
            "**Machine Learning** e **IA** com base de conhecimento."
        )
        st.divider()
        if st.button("Limpar Conversa"):
            st.session_state.messages = []
            st.rerun()
        st.divider()
        st.markdown("**Autor:** Gabriel Demetrios Lafis")
        st.markdown("[GitHub](https://github.com/galafis) | "
                    "[LinkedIn](https://linkedin.com/in/gabriel-demetrios-lafis)")

    # Inicializar agente
    try:
        agent = init_agent()
    except Exception as e:
        st.error(f"Erro ao inicializar: {e}")
        st.stop()

    # Historico de mensagens
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input do usuario
    if prompt := st.chat_input("Faca sua pergunta sobre dados e IA..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                response = agent.ask(prompt)
            st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        # Metricas na sidebar
        with st.sidebar:
            metrics = agent.get_metrics()
            st.metric("Consultas", metrics["queries"])
            st.metric("Tempo Medio", f"{metrics['avg_time']:.2f}s")


if __name__ == "__main__":
    main()
