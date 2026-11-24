import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Upload e Download",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Upload e Download de Dados")

st.write(
    "Importe arquivos CSV para analisar "
    "e exportar dados climáticos."
)

colunas = [
    "cidade",
    "horario",
    "temperatura",
    "umidade",
    "precipitacao",
    "vento"
]

if "dados_importados" not in st.session_state:
    st.session_state.dados_importados = pd.DataFrame(
        columns=colunas
    )

st.subheader("Importar arquivo CSV")

arquivo = st.file_uploader(
    "Selecione um arquivo CSV",
    type=["csv"]
)

if arquivo is not None:

    try:
        df = pd.read_csv(arquivo)

        if all(c in df.columns for c in colunas):

            st.subheader("Prévia dos dados")
            st.dataframe(df, use_container_width=True)

            if st.button("Importar dados"):

                st.session_state.dados_importados = pd.concat(
                    [
                        st.session_state.dados_importados,
                        df[colunas]
                    ],
                    ignore_index=True
                ).drop_duplicates()

                st.success("Dados importados com sucesso!")

        else:
            st.error(
                "O arquivo não possui todas as colunas necessárias."
            )

            st.write("Colunas esperadas:", colunas)

    except Exception as erro:
        st.error(f"Erro ao importar arquivo: {erro}")

st.subheader("Dados importados")

dados = st.session_state.dados_importados

st.metric("Total de registros", len(dados))

st.dataframe(dados, use_container_width=True)

if not dados.empty:

    st.subheader("Estatísticas descritivas")

    st.dataframe(
        dados.describe(include="all"),
        use_container_width=True
    )

    st.download_button(
        label="Baixar dados importados",
        data=dados.to_csv(index=False).encode("utf-8-sig"),
        file_name="dados_importados.csv",
        mime="text/csv"
    )

if st.button("Limpar dados importados"):

    st.session_state.dados_importados = pd.DataFrame(
        columns=colunas
    )

    st.rerun()