import streamlit as st
import base64
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from modelImg import process_image
from modelVideo import process_video

load_dotenv('./.env')

api_key = os.getenv("API_KEY")  
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=api_key)

with open("contexto.txt", "r", encoding="utf-8") as file:
    texto = file.read()


# Inicialização do estado da sessão no Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=f"Você é um assistente da pizzaria La Bella Pizza. Use o seguinte contexto para responder as perguntas {texto}"
                      "caso a pegunta do usuário fuja do contexto da pizzaria La Bella Pizza, responda, Desculpe, mas não posso ajudar,"
                      "mais alguma pergunta?"
                      ),
        AIMessage(content="Seja bem-vindo à La Bella Pizza! 😄 Em que posso ajudar? 🍕🍷 ")
    ]

# Iniciando o Streamlit
st.title("Bella Pizza")
st.write("Telefone: (11) 4000-1234 / WhatsApp: (11) 90000-1234 / Email: contato@labellapizza.com.br")
user_input = st.chat_input("Digite sua pergunta")


def generate_response(human_input=None, uploaded_image=None):
    
    if human_input:
        st.session_state.messages.append(HumanMessage(content=human_input))
        st.chat_message("user").write(human_input)
        response = llm.invoke(st.session_state.messages)
        response = response.content
        
    elif uploaded_image:
        img_base64 = base64.b64encode(uploaded_image.read()).decode("utf-8")
        response = process_image(img_base64)
        
    st.session_state.messages.append(AIMessage(content=response))
    return response

#upload imagem
st.sidebar.header("Faça o upload da imagem de uma pizza aqui para descobrir o sabor e se temos disponível")
uploaded_image = st.sidebar.file_uploader("Escolha uma imagem", type=["png", "jpg", "jpeg"])
if uploaded_image:
    st.sidebar.image(uploaded_image)

#upload video 
uploaded_video = st.sidebar.file_uploader("Escolha um vídeo", type=["mp4", "mov", "avi"])
if uploaded_video and uploaded_image is None and user_input is None:
    st.sidebar.video(uploaded_video)
    response = process_video(uploaded_video, "descreva o que esta acontecendo no video com o maximo de detalhes possíveis, voce é especialista em pizzas"
                  "caso o video nao tenha conexao com a pizzaria ou pizzas em geral, reponda que não pode ajudar com isso"
                  "apenas com assuntos relacionados a pizzaria"
                  )
    st.chat_message("ai").write(response)
    
# Mostrar o chat
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        st.chat_message("user").write(message.content)  
    elif isinstance(message, AIMessage):
        st.chat_message("ai").write(message.content)

# responder imagem
if uploaded_image and user_input is None:
    response = generate_response(uploaded_image=uploaded_image)
    st.chat_message("ai").write(response)
    
# responder msg
if user_input:
    response = generate_response(human_input=user_input)
    st.chat_message("ai").write(response)
