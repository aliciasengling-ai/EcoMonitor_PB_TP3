import streamlit as st
import pandas as pd
from pathlib import Path
from wordcloud import WordCloud
from collections import Counter
import re

st.set_page_config(
    page_title="Conteúdo Ambiental",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Conteúdo Ambiental")

st.write("Análise de conteúdos relacionados à Agenda 2030 e aos ODS.")

st.markdown("""
### Objetivos de Desenvolvimento Sustentável

- ODS 11: Cidades e comunidades sustentáveis.
- ODS 13: Ação contra a mudança global do clima.
""")

arquivo = (
    Path(__file__).resolve().parents[1]
    / "data" / "raw" / "agenda2030.csv"
)

if arquivo.exists():

    df = pd.read_csv(arquivo)

    st.metric("Registros coletados", len(df))

    st.subheader("Conteúdos coletados")

    busca = st.text_input("Pesquisar palavra ou assunto")

    if busca:
        df = df[
            df["texto"].astype(str).str.contains(
                busca, case=False, regex=False, na=False
            )
        ]

    st.dataframe(df, use_container_width=True)

    texto = " ".join(df["texto"].dropna().astype(str))

    palavras_ignoradas = {
        "de", "da", "do", "das", "dos", "a", "o",
        "e", "em", "para", "com", "que", "os",
        "as", "um", "uma", "por", "se", "na",
        "no", "ao", "foi", "são", "mais", "como"
    }

    palavras = [
        p for p in re.findall(r"\b\w+\b", texto.lower())
        if p not in palavras_ignoradas
        and len(p) > 2
        and not p.isdigit()
    ]

    if palavras:

        st.subheader("Nuvem de palavras")

        nuvem = WordCloud(
            width=1000,
            height=450,
            background_color="white",
            colormap="Greens"
        ).generate(" ".join(palavras))

        st.image(nuvem.to_array())

        st.subheader("Palavras mais frequentes")

        frequencia = pd.DataFrame(
            Counter(palavras).most_common(15),
            columns=["palavra", "frequencia"]
        )

        st.bar_chart(
            frequencia.set_index("palavra")
        )

    st.download_button(
        "Baixar conteúdo ambiental",
        df.to_csv(index=False).encode("utf-8-sig"),
        file_name="conteudo_ambiental.csv",
        mime="text/csv"
    )

else:
    st.warning(
        "Arquivo não encontrado. Execute src/scraping.py."
    )

st.subheader("Preparação para Inteligência Artificial")

st.info("""
Na próxima etapa, os textos coletados poderão ser
utilizados com LLMs para gerar resumos automáticos,
classificar conteúdos e responder perguntas sobre
sustentabilidade e Agenda 2030.
""")