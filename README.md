# AI Virtual Assistant - Generative AI

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)](https://openai.com)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-orange.svg)](https://langchain.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Sobre o Projeto

Assistente Virtual inteligente construido com **IA Generativa**, utilizando **LangChain**, **OpenAI GPT** e tecnicas de **RAG (Retrieval-Augmented Generation)** para fornecer respostas contextualizadas baseadas em uma base de conhecimento customizada.

Projeto Final desenvolvido como parte do bootcamp **Bradesco GenAI & Dados** na plataforma **DIO**.

## Arquitetura

```
Usuario -> Interface (Streamlit) -> Agente IA
                                      |
                              +-------+-------+
                              |               |
                        Base de          OpenAI GPT
                       Conhecimento      (LLM)
                        (FAISS)          
                              |               |
                              +-------+-------+
                                      |
                              Resposta Contextualizada
```

## Etapas do Projeto

### Etapa 1: Documentacao do Agente
- Definicao do proposito e escopo do assistente
- Persona: Assistente especialista em dados e IA
- Publico-alvo: Profissionais e estudantes de tecnologia

### Etapa 2: Base de Conhecimento
- Documentos sobre Data Science, Machine Learning e IA
- Indexacao vetorial com FAISS
- Embeddings via OpenAI

### Etapa 3: Prompts do Agente
- System prompt otimizado para respostas precisas
- Chain of Thought para raciocinio estruturado
- Tratamento de contexto e historico de conversas

### Etapa 4: Aplicacao Funcional
- Interface web com Streamlit
- Pipeline RAG completo
- Historico de conversas persistente

### Etapa 5: Avaliacao e Metricas
- Relevancia das respostas
- Tempo de resposta
- Cobertura da base de conhecimento

### Etapa 6: Pitch
- Apresentacao do projeto e resultados

## Tecnologias Utilizadas

- **Python 3.9+**
- **LangChain** - Framework para aplicacoes com LLMs
- **OpenAI GPT API** - Modelo de linguagem
- **FAISS** - Busca vetorial eficiente
- **Streamlit** - Interface web interativa
- **python-dotenv** - Gerenciamento de variaveis de ambiente

## Instalacao

```bash
git clone https://github.com/galafis/ai-virtual-assistant-generative.git
cd ai-virtual-assistant-generative

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

## Configuracao

```bash
cp .env.example .env
# Edite o .env com sua OPENAI_API_KEY
```

## Como Usar

```bash
# Interface web
streamlit run app.py

# Modo terminal
python main.py
```

## Estrutura do Projeto

```
ai-virtual-assistant-generative/
|-- app.py                  # Interface Streamlit
|-- main.py                 # Modo terminal
|-- agent.py                # Logica do agente IA
|-- knowledge_base.py       # Base de conhecimento e RAG
|-- config.py               # Configuracoes
|-- prompts.py              # Templates de prompts
|-- requirements.txt        # Dependencias
|-- .env.example            # Exemplo de variaveis
|-- docs/                   # Documentos da base de conhecimento
|   |-- data_science.txt
|   |-- machine_learning.txt
|   |-- ia_generativa.txt
|-- LICENSE
|-- README.md
```

## Autor

**Gabriel Demetrios Lafis**

- LinkedIn: [gabriel-demetrios-lafis](https://www.linkedin.com/in/gabriel-demetrios-lafis/)
- GitHub: [galafis](https://github.com/galafis)

---

> Projeto Final desenvolvido durante o bootcamp **Bradesco GenAI & Dados** - [DIO](https://www.dio.me/)
