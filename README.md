# EcoMonitor Brasil — TP2
Evolução do TP1 (ODS 11 e 13). Python 3.11–3.13 recomendado.
No PowerShell, dentro da pasta do projeto:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src/scraping.py
.\.venv\Scripts\python.exe -m streamlit run app.py
```
Antes da coleta, confira os termos de uso da ONU Brasil. Se a coleta for bloqueada, não contorne o bloqueio. Consulte docs e tests. Para deploy no Streamlit Community Cloud, selecione o repositório e app.py; inclua o CSV coletado se sua redistribuição for permitida. Não publique dados pessoais nem o ambiente virtual.
