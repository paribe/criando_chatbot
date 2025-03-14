import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

# Definir a chave da API
api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

# Inicializar o modelo de IA
chat = ChatGroq(model='llama-3.3-70b-versatile')

# Função para obter resposta do bot
def resposta_do_bot(pergunta):
    system_message = 'Você é um assistente amigável chamado ChatBot (Davi)'
    template = ChatPromptTemplate.from_messages([
        ('system', system_message),
        ('user', pergunta)
    ])
    chain = template | chat
    return chain.invoke({}).content

# Interface com Streamlit
st.title("🤖 ChatBot (Davi) - Seu Assistente Virtual")

# Inicializar o estado da sessão para a pergunta atual e resposta
if "pergunta_atual" not in st.session_state:
    st.session_state.pergunta_atual = None
    
if "resposta_atual" not in st.session_state:
    st.session_state.resposta_atual = None

# Campo de entrada para o usuário
pergunta = st.chat_input("Digite sua pergunta...")

if pergunta:
    # Atualizar a pergunta atual
    st.session_state.pergunta_atual = pergunta
    
    # Obter resposta do bot
    resposta = resposta_do_bot(pergunta)
    st.session_state.resposta_atual = resposta
    
    # Limpar a interface (não necessário, o Streamlit recarrega a página)
    
# Exibir apenas a conversa atual, se existir
if st.session_state.pergunta_atual:
    st.chat_message("user").write(st.session_state.pergunta_atual)
    
if st.session_state.resposta_atual:
    st.chat_message("assistant").write(st.session_state.resposta_atual)
