# Planejamento para integração com LLMs

## EcoMonitor Brasil — TP3

### Objetivo

Preparar o EcoMonitor Brasil para a futura integração com modelos de linguagem de grande escala (LLMs), ampliando suas funcionalidades de análise ambiental e sustentabilidade.

### Dados disponíveis

- Indicadores climáticos obtidos pela API Open-Meteo.
- Conteúdos relacionados à sustentabilidade e à Agenda 2030.
- Arquivos CSV importados pelos usuários.
- Registros consultados e adicionados por meio da FastAPI.

### Aplicações futuras

**1. Resumos automáticos**

Utilizar LLMs para resumir conteúdos ambientais e documentos relacionados aos Objetivos de Desenvolvimento Sustentável.

**2. Perguntas e respostas**

Criar um assistente inteligente capaz de responder perguntas sobre sustentabilidade e indicadores climáticos.

**3. Geração de relatórios**

Produzir relatórios descritivos com base nos indicadores de temperatura, umidade, precipitação e velocidade do vento.

**4. Análise de sentimentos**

Avaliar futuramente textos e notícias ambientais, classificando-os como positivos, negativos ou neutros.

### Arquitetura planejada

A aplicação Streamlit será responsável pela interação com o usuário. A FastAPI será utilizada como camada de comunicação com os dados e, futuramente, com os modelos de linguagem.

### Segurança e qualidade

Os dados deverão ser validados antes do processamento. As respostas geradas pela inteligência artificial deverão ser verificadas para evitar informações incorretas e conclusões sem fundamentação.

### Conclusão

Nesta etapa, o projeto estabelece a base tecnológica e documental para a futura integração com LLMs. A implementação efetiva dos modelos será realizada nas próximas fases do desenvolvimento.