import streamlit as st

st.set_page_config(
    page_title="EcoMonitor Brasil - TP3",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 EcoMonitor Brasil")

st.subheader("Monitoramento ambiental e sustentabilidade")

st.markdown("""
### Sobre o projeto

O EcoMonitor Brasil é uma aplicação voltada
ao monitoramento de indicadores climáticos,
sustentabilidade e Agenda 2030.

Nesta terceira etapa, o projeto foi ampliado
com múltiplas páginas e integração com FastAPI.

### Funcionalidades

- Consulta de dados climáticos.
- Visualização de indicadores ambientais.
- Coleta de conteúdo sobre sustentabilidade.
- Upload e download de arquivos CSV.
- Consulta e envio de dados via FastAPI.
- Preparação para futura integração com LLMs.

### Navegação

Utilize o menu lateral para acessar as
funcionalidades disponíveis.
""")

st.divider()

st.info(
    "Projeto acadêmico — EcoMonitor Brasil | PB TP3"
)

st.markdown(
    "[Agenda 2030](https://brasil.un.org/pt-br/sdgs)"
    " | "
    "[Open-Meteo](https://open-meteo.com/)"
)