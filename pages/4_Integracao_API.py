import streamlit as st
import pandas as pd
import requests
from datetime import datetime

st.set_page_config(
    page_title="Integração API",
    page_icon="🔗",
    layout="wide"
)

st.title("🔗 Integração com FastAPI")

st.write(
    "Consulte e envie dados climáticos "
    "através da API do EcoMonitor Brasil."
)

API_URL = "http://127.0.0.1:8000"

st.subheader("Status da API")

try:
    resposta = requests.get(API_URL, timeout=5)
    resposta.raise_for_status()
    st.success("API conectada com sucesso!")

except requests.RequestException:
    st.error("API desconectada. Inicie o FastAPI.")

st.markdown(
    "[Documentação da API - Swagger]"
    "(http://127.0.0.1:8000/docs)"
)

st.divider()

st.subheader("Consultar dados — GET")

if st.button("Consultar dados da API"):

    try:
        resposta = requests.get(
            f"{API_URL}/dados",
            timeout=10
        )

        resposta.raise_for_status()

        st.success("Consulta realizada com sucesso!")

        dados = resposta.json()

        st.json(dados)

    except Exception as erro:
        st.error(f"Erro na consulta: {erro}")

st.divider()

st.subheader("Adicionar dados — POST")

with st.form("formulario_api"):

    cidade = st.text_input("Cidade")

    temperatura = st.number_input(
        "Temperatura (°C)",
        value=25.0
    )

    umidade = st.number_input(
        "Umidade (%)",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

    precipitacao = st.number_input(
        "Precipitação (mm)",
        min_value=0.0
    )

    vento = st.number_input(
        "Velocidade do vento (km/h)",
        min_value=0.0
    )

    enviar = st.form_submit_button(
        "Enviar dados para a API"
    )

if enviar:

    if not cidade.strip():

        st.warning("Informe o nome da cidade.")

    else:

        dados = {
            "cidade": cidade.strip(),
            "horario": datetime.now().isoformat(
                timespec="seconds"
            ),
            "temperatura": temperatura,
            "umidade": umidade,
            "precipitacao": precipitacao,
            "vento": vento
        }

        try:

            resposta = requests.post(
                f"{API_URL}/dados",
                json=dados,
                timeout=10
            )

            resposta.raise_for_status()

            st.success("Dados enviados com sucesso!")

            st.json(resposta.json())

        except Exception as erro:

            st.error(f"Erro no envio: {erro}")