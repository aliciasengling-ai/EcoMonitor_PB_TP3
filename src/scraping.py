
from pathlib import Path
from urllib.robotparser import RobotFileParser
from datetime import datetime, timezone
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://pt.wikipedia.org/wiki/Objetivos_de_Desenvolvimento_Sustent%C3%A1vel"
ROBOTS = "https://pt.wikipedia.org/robots.txt"

AGENT = "EcoMonitorAcademic/1.0"

OUT = (
    Path(__file__).resolve().parents[1]
    / "data/raw/agenda2030.csv"
)

def extrair():
    headers = {"User-Agent": AGENT}

    resposta = requests.get(
        ROBOTS, headers=headers, timeout=30
    )
    resposta.raise_for_status()

    robots = RobotFileParser()
    robots.parse(resposta.text.splitlines())

    if not robots.can_fetch(AGENT, URL):
        raise RuntimeError("Coleta não permitida.")

    pagina = requests.get(
        URL,
        headers=headers,
        timeout=30,
        allow_redirects=False
    )
    pagina.raise_for_status()

    if pagina.status_code != 200:
        raise RuntimeError("Verifique a URL da fonte.")

    soup = BeautifulSoup(pagina.text, "html.parser")

    conteudo = soup.find(
        "div", class_="mw-parser-output"
    ) or soup

    textos = []

    for p in conteudo.find_all("p"):
        texto = p.get_text(" ", strip=True)
        if len(texto) > 50:
            textos.append(texto)

    if not textos:
        raise RuntimeError("Nenhum conteúdo encontrado.")

    df = pd.DataFrame({
        "texto": textos,
        "fonte": URL,
        "coletado_em": datetime.now(timezone.utc).isoformat()
    })

    OUT.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        OUT, index=False, encoding="utf-8-sig"
    )

    print("Coleta realizada com sucesso!")
    print(f"Registros coletados: {len(df)}")
    print(f"Arquivo salvo em: {OUT}")

if __name__ == "__main__":
    extrair()
