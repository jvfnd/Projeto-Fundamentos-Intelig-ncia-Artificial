import streamlit as st
from google import generativeai as genai

api_key = st.secrets['API_KEY']
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

st.title("Análise de Texto com IA")
task = st.selectbox(
    "Selecione a tarefa de IA",
    ["Resumo", "Tradução para Português", "Análise de Sentimento", "Correção Gramatical", 
     "Buscar Fontes", "Classificação de Texto", "Resenha Crítica"])

def analise_texto(texto):
    if task == "Resumo":
        prompt = f"Resuma o seguinte texto: {texto}"
    elif task == "Tradução para Português":
        prompt = f"Traduza o seguinte texto para o português: {texto}"
    elif task == "Análise de Sentimento":
        prompt = f"Analise o sentimento do seguinte texto: {texto}"
    elif task == "Correção Gramatical":
        prompt = f"Corrija gramaticalmente o seguinte texto: {texto}"
    elif task == "Buscar Fontes":
        prompt = f"Busque fontes confiáveis para o seguinte texto: {texto}"
    elif task == "Classificação de Texto":
        prompt = f"Classifique o seguinte texto em categorias: {texto}"    
    elif task == "Resenha Crítica"
        prompt = f"Escreva uma resenha crítica do seguinte texto, destacando pontos fortes, fracos e possíveis interpretações: {texto}"
    else:
        st.error("Tarefa não reconhecida.")
        return
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
