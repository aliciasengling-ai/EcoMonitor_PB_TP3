import streamlit as st
import pandas as pd
import requests

st.set_page_config(
    page_title="Clima",
    page_icon="🌦️",
    layout="wide"
)

st.title("🌦️ Monitoramento Climático")

st.write("Consulta de indicadores climáticos via Open-Meteo.")

cidades = {
    "São Paulo": (-23.55, -46.63),
    "Rio de Janeiro": (-22.91, -43.17),
    "Brasília": (-15.79, -47.88),
    "Curitiba": (-25.43, -49.27),
    "Salvador": (-12.97, -38.50)
}

cidade = st.selectbox("Selecione a cidade", list(cidades))

latitude, longitude = cidades[cidade]

url = "https://api.open-meteo.com/v1/forecast"

parametros = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": (
        "temperature_2m,relative_humidity_2m,"
        "precipitation,wind_speed_10m"
    ),
    "forecast_days": 1,
    "timezone": "America/Sao_Paulo"
}

try:
    resposta = requests.get(
        url, params=parametros, timeout=30
    )
    resposta.raise_for_status()

    dados = resposta.json()["hourly"]

    df = pd.DataFrame(dados)

    df.columns = [
        "horario",
        "temperatura",
        "umidade",
        "precipitacao",
        "vento"
    ]

    df["horario"] = pd.to_datetime(df["horario"])

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Temperatura média",
        f"{df['temperatura'].mean():.1f} °C"
    )

    col2.metric(
        "Umidade média",
        f"{df['umidade'].mean():.1f}%"
    )

    col3.metric(
        "Precipitação total",
        f"{df['precipitacao'].sum():.1f} mm"
    )

    st.subheader("Dados climáticos")

    st.dataframe(df, use_container_width=True)

    indicador = st.selectbox(
        "Escolha o indicador",
        ["temperatura", "umidade", "precipitacao", "vento"]
    )

    st.subheader("Gráfico interativo")

    st.line_chart(df.set_index("horario")[indicador])

    st.download_button(
        "Baixar dados climáticos",
        df.to_csv(index=False).encode("utf-8-sig"),
        file_name="dados_climaticos.csv",
        mime="text/csv"
    )

except Exception as erro:
    st.error(f"Erro ao consultar a API: {erro}")