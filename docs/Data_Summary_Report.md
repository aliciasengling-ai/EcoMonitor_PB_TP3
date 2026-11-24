# Data Summary Report

Open-Meteo — https://open-meteo.com/en/docs — API JSON de previsão meteorológica; temperatura (°C), umidade (%), precipitação (mm), vento (km/h), horário local. Uso: acompanhamento de condições meteorológicas previstas; não confundir previsão com observação. Consulta por latitude e longitude de São Paulo. Integração opcional no código; disponibilidade e condições de uso devem ser verificadas.
IBGE — https://servicodados.ibge.gov.br/api/docs/localidades — API JSON de localidades, códigos e nomes de municípios; uso futuro: seleção territorial e padronização de nomes. Não integrada no TP1.
Amostra local: data/raw/amostra.csv, três registros fictícios para testar a interface, sem valor científico. Campos: cidade, horario, temperatura, umidade, precipitacao, vento. Qualidade planejada: verificar nulos, duplicatas, tipos, umidade entre 0 e 100 e precipitação não negativa. Registrar origem e horário de coleta. Não coletar dados pessoais.
## TP2
ONU Brasil: https://brasil.un.org/pt-br/sdgs/13 — HTML público, extração de títulos e parágrafos com Beautiful Soup, condicionada a permissões e termos de uso. Saída data/raw/agenda2030.csv: texto, fonte, coletado_em (UTC). Uso: frequência de termos e nuvem de palavras; não representa notícias nem opinião pública. Coleta ainda não executada neste ambiente. Upload: CSV com as seis colunas da amostra, origem identificada como usuário, validação de tipos e limites, remoção de duplicatas exatas no upload. Dados importados ficam na sessão, não em armazenamento permanente. IBGE continua planejado, não integrado.
## Atualização do Data Summary Report — TP3

**Projeto:** EcoMonitor Brasil

**Responsável:** Alicia Scripelliti

### 1. Descrição dos dados

O projeto utiliza dados climáticos e conteúdos relacionados ao meio ambiente, à sustentabilidade e à Agenda 2030.

### 2. Fontes de dados

- Open-Meteo: obtenção de informações climáticas.
- Web scraping com Beautiful Soup: extração de conteúdos ambientais.
- Arquivos CSV: armazenamento e organização dos registros.
- FastAPI: consulta e inclusão de registros climáticos.

### 3. Estrutura dos dados climáticos

| Campo | Descrição |
|---|---|
| cidade | Localidade analisada |
| horario | Data e horário do registro |
| temperatura | Temperatura em graus Celsius |
| umidade | Umidade relativa do ar |
| precipitacao | Precipitação em milímetros |
| vento | Velocidade do vento em km/h |

### 4. Armazenamento e organização

Os arquivos de dados são organizados no diretório data/ do projeto, permitindo sua utilização nas análises e visualizações da aplicação Streamlit.

### 5. Integração com FastAPI

A API desenvolvida disponibiliza os seguintes endpoints:

| Método | Endpoint | Finalidade |
|---|---|---|
| GET | / | Verificar o funcionamento da API |
| GET | /dados | Consultar registros climáticos |
| POST | /dados | Adicionar novos registros |
| GET | /docs | Acessar a documentação Swagger |

### 6. Validação e testes

Foram realizados testes de comunicação entre Streamlit e FastAPI, obtendo os seguintes resultados:

- Conexão com a API realizada com sucesso.
- Consulta GET executada com retorno HTTP 200.
- Envio POST executado com retorno HTTP 201.
- Exibição dos registros na interface Streamlit.

Os registros fictícios utilizados nos testes devem ser identificados e separados dos dados reais antes das análises.

### 7. Decisão sobre Selenium

Nesta etapa, priorizou-se a utilização de APIs e Beautiful Soup, mantendo a simplicidade da arquitetura. O Selenium poderá ser incorporado futuramente caso novas fontes exijam interação com páginas dinâmicas.

### 8. Preparação para integração com LLMs

Os dados estruturados e os conteúdos ambientais poderão ser utilizados futuramente em aplicações de inteligência artificial, incluindo:

- Geração automática de relatórios ambientais.
- Resumos de conteúdos sobre sustentabilidade.
- Classificação de sentimentos em textos ambientais.
- Assistente inteligente de perguntas e respostas.
- Geração de insights a partir dos indicadores climáticos.

Os cálculos estatísticos deverão ser realizados com Python, utilizando os LLMs para interpretação e comunicação dos resultados.

### 9. Limitações

A qualidade das análises depende da disponibilidade, atualização e confiabilidade das fontes. Os dados deverão ser validados antes de serem utilizados por modelos de linguagem.

### 10. Conclusão

A evolução do EcoMonitor Brasil no TP3 amplia as possibilidades de interação com os dados por meio de múltiplas páginas e integração com FastAPI, preparando a aplicação para a futura incorporação de inteligência artificial.