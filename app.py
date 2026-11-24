from pathlib import Path
from collections import Counter
import re
import pandas as pd
import streamlit as st
from wordcloud import WordCloud
from src.coleta import coletar

ROOT = Path(__file__).parent
METRICAS = ['temperatura', 'umidade', 'precipitacao', 'vento']
COLUNAS = ['cidade', 'horario'] + METRICAS
st.set_page_config(page_title='EcoMonitor Brasil', page_icon='🌱', layout='wide')

@st.cache_data(ttl=900)
def previsao():
    return coletar()

@st.cache_data
def ler_csv(caminho, versao):
    return pd.read_csv(caminho)

st.session_state.setdefault('extras', pd.DataFrame(columns=COLUNAS))
st.title('EcoMonitor Brasil | TP2')
st.caption('ESG ambiental • ODS 11 e 13')
st.write('Centralização de indicadores climáticos e conteúdo ambiental para gestores, empresas e ONGs.')
st.markdown('[Agenda 2030](https://brasil.un.org/pt-br/sdgs) | [Open-Meteo](https://open-meteo.com/en/docs)')
aba = st.sidebar.radio('Navegação', ['Clima', 'Conteúdo ambiental', 'Upload e download'])
if aba == 'Upload e download':
    st.subheader('Adicionar dados climáticos')
    st.write('CSV separado por vírgulas, com colunas: ' + ', '.join(COLUNAS))
    arq = st.file_uploader('Selecione um CSV', type='csv')
    if st.button('Importar dados', disabled=arq is None):
        try:
            d = pd.read_csv(arq)
            d = d[COLUNAS].copy()
            d['horario'] = pd.to_datetime(d['horario'], format='mixed', errors='raise').astype(str)
            for c in METRICAS:
                d[c] = pd.to_numeric(d[c], errors='raise')
            if d.empty or d.isna().any().any() or not d.umidade.between(0,100).all() or (d[['precipitacao','vento']] < 0).any().any():
                raise ValueError('Dados vazios, ausentes ou fora dos limites.')
            st.session_state.extras = pd.concat([st.session_state.extras,d], ignore_index=True).drop_duplicates()
            st.success('Dados adicionados à sessão.')
        except Exception as e:
            st.error(f'CSV inválido: {e}')
    if st.button('Limpar dados importados'):
        st.session_state.extras = pd.DataFrame(columns=COLUNAS)
    st.dataframe(st.session_state.extras)
    st.download_button('Baixar dados importados', st.session_state.extras.to_csv(index=False).encode('utf-8-sig'), 'importados.csv', 'text/csv')
elif aba == 'Conteúdo ambiental':
    st.subheader('Conteúdo da Agenda 2030')
    p = ROOT / 'data/raw/agenda2030.csv'
    if not p.exists():
        st.warning('Execute python src/scraping.py para gerar o CSV de conteúdo ambiental.')
    else:
        d = ler_csv(str(p), p.stat().st_mtime_ns)
        st.dataframe(d)
        stop = set('para com uma dos das que por não são mais como seu sua seus suas pelo pela sobre entre este esta isso esse essa aos nas nos tem ser das ao de da do em os as um se na no ou e a o é'.split())
        palavras = [w for w in re.findall(r'[^\W\d_]+', ' '.join(d.texto.fillna('').astype(str)).lower()) if len(w)>2 and w not in stop]
        freq = Counter(palavras)
        st.metric('Trechos coletados', len(d))
        st.metric('Palavras distintas', len(freq))
        if freq:
            st.image(WordCloud(width=900,height=400,background_color='white').generate_from_frequencies(freq).to_array())
            st.bar_chart(pd.DataFrame(freq.most_common(15), columns=['palavra','frequencia']).set_index('palavra'))
else:
    p = ROOT / 'data/raw/amostra.csv'
    d = ler_csv(str(p), p.stat().st_mtime_ns).assign(origem='Amostra fictícia')
    if st.sidebar.checkbox('Consultar API Open-Meteo'):
        try:
            d = previsao().assign(origem='Previsão Open-Meteo')
        except Exception as e:
            st.warning(f'API indisponível; exibindo amostra fictícia. {e}')
    d = pd.concat([d, st.session_state.extras.assign(origem='Upload do usuário')], ignore_index=True)
    cidades = st.sidebar.multiselect('Cidades', sorted(d.cidade.unique()), default=sorted(d.cidade.unique()))
    origens = st.sidebar.multiselect('Origem', sorted(d.origem.unique()), default=sorted(d.origem.unique()))
    d = d[d.cidade.isin(cidades) & d.origem.isin(origens)].copy()
    indicador = st.sidebar.selectbox('Indicador', METRICAS)
    st.caption('Temperatura °C | Umidade % | Precipitação mm | Vento km/h')
    if not d.empty:
        st.metric('Registros', len(d))
        st.metric('Completude', f'{d[METRICAS].notna().mean().mean():.1%}')
        st.dataframe(d)
        d['horario'] = pd.to_datetime(d.horario, format='mixed', errors='coerce')
        d['serie'] = d.cidade + ' / ' + d.origem
        st.line_chart(d, x='horario', y=indicador, color='serie')
        st.bar_chart(d.groupby('serie')[indicador].mean())
    else:
        st.info('Nenhum registro para os filtros selecionados.')
    st.download_button('Baixar dados filtrados', d.to_csv(index=False).encode('utf-8-sig'), 'clima.csv', 'text/csv')
