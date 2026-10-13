import streamlit as st

from prompts import obter_prompt_sistema
from memory import carregar_historico, salvar_historico
from ai_client import chat_completions, GroqAPIError
from utils import limitar_historico

st.set_page_config(page_title="Meu Primeiro Chatbot Inteligente", page_icon="🤖")

st.title("🤖 Meu Primeiro Chatbot Inteligente")
st.caption("Python + Groq API + Streamlit — projeto final do Nível 5")

tema = st.selectbox("Tema do assistente", ["estudos", "motivacional", "filmes"], index=0)
system_prompt = obter_prompt_sistema(tema)

if "mensagens" not in st.session_state:
    historico = carregar_historico()
    st.session_state.mensagens = [{"role": "system", "content": system_prompt}] + historico

st.session_state.mensagens[0] = {"role": "system", "content": system_prompt}

for m in st.session_state.mensagens:
    if m["role"] == "system":
        continue
    with st.chat_message(m["role"]):
        st.write(m["content"])

user_text = st.chat_input("Digite sua mensagem...")

if user_text:
    st.session_state.mensagens.append({"role": "user", "content": user_text})
    st.session_state.mensagens = limitar_historico(st.session_state.mensagens, max_itens=14)

    try:
        resposta = chat_completions(st.session_state.mensagens)
    except GroqAPIError as e:
        st.error(str(e))
    else:
        st.session_state.mensagens.append({"role": "assistant", "content": resposta})
        salvar_historico([m for m in st.session_state.mensagens if m["role"] != "system"])
        st.rerun()