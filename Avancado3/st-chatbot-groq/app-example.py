import streamlit as st
from groq import Groq
from config_token import V_GROQ
from config_token import V_MODELO
from config_token import V_MODELO_AUDIO
from config_token import V_MODELO_TO_AUDIO

# ---------- Configuração inicial ----------
st.set_page_config(page_title="Chatbot com Groq (Streamlit)", page_icon="💬")

if not V_GROQ:
    st.error('Defina a variável GROQ_TOKEN no arquivo .env para continuar.')
    st.stop()

client = Groq(api_key=V_GROQ)

# ---------- Estado da aplicação ----------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "Você é um assistente útil e objetivo. Responda em português do Brasil."
        }
    ]

# ---------- Sidebar ----------
st.sidebar.header("⚙️ Configurações")

model = st.sidebar.selectbox(
    "Modelo",
    options=[
        V_MODELO, V_MODELO_AUDIO, V_MODELO_TO_AUDIO,
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile",
    ],
    index=0,
    help="8B tende a ser mais rápido; 70B tende a entregar respostas mais elaboradas."
)

temperature = st.sidebar.slider("Temperatura", 0.0, 1.0, 0.2, 0.1)
max_tokens = st.sidebar.slider("Máx. tokens de resposta", 128, 1024, 512, 128)

if st.sidebar.button("Limpar conversa"):
    st.session_state.messages = st.session_state.messages[:1]  # preserva system message
    st.rerun()

st.title("💬 Chatbot com Streamlit + Groq")
st.caption("Exemplo didático: histórico, streaming e seleção de modelo.")

# ---------- Renderiza histórico ----------
for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

# ---------- Entrada do usuário ----------
if prompt := st.chat_input("Digite sua mensagem..."):
    # 1) mostra e registra a mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2) placeholder para a resposta do assistente
    with st.chat_message("assistant"):
        response_container = st.empty()
        accumulated = ""

        # Chamada à API com streaming (token a token)
        stream = client.chat.completions.create(
            model=model,
            messages=st.session_state.messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
        )

        for chunk in stream:
            delta = chunk.choices[0].delta
            if hasattr(delta, "content") and delta.content:
                accumulated += delta.content
                response_container.markdown(accumulated)

        # 3) salva a resposta final no histórico
        st.session_state.messages.append({"role": "assistant", "content": accumulated})