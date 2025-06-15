import streamlit as st
from google import generativeai as genai

api_key = st.secrets('API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

def analise_texto(texto):
    prompt = f"Analise o seguinte texto e forneça um resumo: {texto}"
    response = model.generate_content(prompt)
    return response.text

texto = st.text_area("Cole o texto aqui para a IA analisar:")


if st.button("Analisar Texto"):
    if texto:
        st.write("Texto analisado com sucesso!")
        resultado = analise_texto(texto)
        st.write("Resultado da análise:", resultado)
    else:
        st.error("Por favor, cole um texto antes de analisar.")
