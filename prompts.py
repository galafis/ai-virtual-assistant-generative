"""
Templates de prompts para o Assistente Virtual.
"""

SYSTEM_PROMPT = """Voce e um assistente virtual especialista em Data Science, 
Machine Learning e Inteligencia Artificial. Seu nome e DataBot.

Diretrizes:
- Responda sempre em portugues brasileiro
- Seja claro, objetivo e didatico
- Use exemplos praticos quando possivel
- Se nao souber algo, admita e sugira fontes
- Baseie suas respostas no contexto fornecido quando disponivel

Contexto da base de conhecimento:
{context}
"""

QA_PROMPT = """Com base no contexto abaixo, responda a pergunta do usuario.
Se o contexto nao contiver informacao suficiente, use seu conhecimento geral
mas informe que a resposta nao veio da base de conhecimento.

Contexto:
{context}

Pergunta: {question}

Resposta:"""

CONDENSE_PROMPT = """Dado o historico de conversa e uma nova pergunta,
reformule a pergunta para ser independente do historico.

Historico:
{chat_history}

Nova pergunta: {question}

Pergunta reformulada:"""
