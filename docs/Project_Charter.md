# Project Charter

Problema: informações climáticas dispersas dificultam o planejamento ambiental de organizações. A solução centraliza indicadores de temperatura, umidade, precipitação e vento. Pilar ESG: ambiental. ODS 13 (ação climática, especialmente conscientização e capacidade de adaptação) e ODS 11 (planejamento de cidades sustentáveis). O painel não mede diretamente emissões nem comprova impacto ambiental.
Público: gestores ambientais, ONGs, empresas, pesquisadores e estudantes. Stakeholders: autora Alicia Scripelliti (desenvolvimento), professor (avaliação) e usuários potenciais (validação futura).
Escopo TP1: planejamento, amostra sintética, demo Streamlit e coleta opcional via API. Fora do escopo atual: alertas oficiais, previsão própria, scraping e LLMs em produção.
Metas: duas fontes integradas até o final do projeto; quatro indicadores; três gráficos; completude mínima de 95% (campos preenchidos / campos esperados); interface validada por três usuários em etapa futura. Critério TP1: abrir a demo, visualizar tabela e identificar fontes. Riscos: indisponibilidade da API, dados faltantes, interpretação incorreta e dependência de internet. Mitigação: timeout, amostra local identificada, validação e documentação de unidades.
## TP2
Escopo: filtros por cidade e origem, gráficos, scraping do ODS 13, frequência de palavras, cache de 15 minutos para API, upload CSV validado, exportação e estado de sessão. Stakeholders e metas do TP1 mantidos; aceitação: executar cada item do roteiro de testes, publicar repositório e documentar evidências. Riscos adicionais: alterações no HTML, permissões de coleta, arquivos inválidos e confusão entre fontes. Mitigação: verificar robots.txt e termos, identificar origem, validar CSV e tratar falhas. LLM e alertas oficiais permanecem fora do escopo.
## Atualização do projeto — TP3

### Projeto: EcoMonitor Brasil

**Responsável:** Alicia Scripelliti

### Problema de negócio

A dificuldade de centralizar, consultar e interpretar informações climáticas e ambientais pode prejudicar a tomada de decisões relacionadas à sustentabilidade.

### Objetivo geral

Desenvolver uma plataforma interativa de monitoramento ambiental, alinhada aos ODS 11 e 13 da Agenda 2030, facilitando o acesso aos indicadores climáticos e aos conteúdos sobre sustentabilidade.

### Público-alvo

Gestores, empresas, organizações não governamentais, estudantes e pesquisadores interessados em sustentabilidade ambiental.

### Evolução do projeto no TP3

- Implementação de múltiplas páginas utilizando Streamlit.
- Criação de um menu lateral de navegação.
- Desenvolvimento de uma API própria utilizando FastAPI.
- Implementação de endpoints GET e POST.
- Integração entre Streamlit e FastAPI.
- Documentação interativa da API por meio do Swagger.
- Preparação para futura utilização de modelos de linguagem (LLMs).

### Tecnologias utilizadas

- Python.
- Streamlit.
- FastAPI.
- Uvicorn.
- Pydantic.
- Pandas.
- Requests.
- Beautiful Soup.
- Open-Meteo.
- Git e GitHub.

### Decisões técnicas

Optou-se pela manutenção da coleta de dados por APIs e Beautiful Soup, considerando que as fontes utilizadas não exigem interação dinâmica com elementos JavaScript. Dessa forma, a utilização do Selenium não é necessária nesta etapa.

### Resultados alcançados

Os testes de integração demonstraram que a aplicação consegue estabelecer comunicação com a FastAPI, consultar registros climáticos e enviar novos dados por meio da interface Streamlit.

### Próximas etapas

Integrar modelos de linguagem para geração automática de relatórios, resumos de conteúdos ambientais e desenvolvimento de um assistente inteligente de perguntas e respostas.