
import streamlit as st
import google.generativeai as genai

# Configura tu API Key de Gemini
genai.configure(api_key="AIzaSyDDgVzgub-2Va_5xCVcKBU_kYtpqpttyfk")
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="VictorIA Nexus", page_icon=":robot_face:", layout="centered")

st.markdown("""
    <style>
    .block-container { padding-bottom: 10rem; }
    .stChatInput {
        position: fixed !important;
        bottom: 4.2rem !important;  /* <-- Ajusta este número si quieres más arriba o más abajo */
        left: 0; width: 100vw !important;
        background: #191c24 !important;
        border-top: 2px solid #3b7de9 !important;
        z-index: 9999 !important;
        padding: 1.2rem 0.5rem 1.2rem 0.5rem !important;
        box-shadow: 0 -2px 14px #1b4a7a22;
    }
    </style>
""", unsafe_allow_html=True)

st.title("VictorIA Nexus")
st.caption("Asistente virtual académico adaptativo. Explicaciones creativas y personalizadas según tu estilo de aprendizaje.")

if "messages" not in st.session_state:
    st.session_state.messages = []

estilo = st.selectbox("Selecciona tu estilo de aprendizaje:", ["Visual", "Auditivo", "Kinestésico"], key="estilo")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Escribe tu consulta académica aquí...")

def construir_prompt(pregunta, estilo):
    base = (
        "Eres VictorIA Nexus, un asistente académico creativo y adaptativo. "
        "Primero, responde de forma concisa y clara a la pregunta, en un solo párrafo. "
        "Luego, proporciona una explicación creativa, profunda y adaptada al estilo de aprendizaje indicado, "
        "usando analogías, metáforas o ejemplos originales, como si explicaras a un estudiante curioso. "
        "Evita respuestas automáticas o superficiales."
    )
    if estilo == "Visual":
        detalle = (
            "La explicación creativa debe incluir un diagrama o esquema visual en arte ASCII, "
            "como cajas, flechas y relaciones, para ilustrar la respuesta. "
            "No expliques otros estilos."
        )
    elif estilo == "Auditivo":
        detalle = (
            "La explicación creativa debe incluir ejemplos auditivos, relatos, metáforas sonoras, explicaciones habladas o historias narradas. "
            "No expliques otros estilos."
        )
    else:
        detalle = (
            "La explicación creativa debe sugerir actividades prácticas, ejemplos kinestésicos, ejercicios paso a paso y propuestas que impliquen acción física. "
            "No expliques otros estilos."
        )
    return f"{base} {detalle} Pregunta: {pregunta}"

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        prompt_full = construir_prompt(prompt, estilo)
        try:
            respuesta = model.generate_content(prompt_full)
            st.markdown(respuesta.text)
            st.session_state.messages.append({"role": "assistant", "content": respuesta.text})
        except Exception as e:
            st.markdown(f"Error al generar respuesta: {e}")
            st.session_state.messages.append({"role": "assistant", "content": f"Error al generar respuesta: {e}"})






