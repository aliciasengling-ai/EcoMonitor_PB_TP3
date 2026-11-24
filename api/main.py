
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pathlib import Path
from datetime import datetime
import pandas as pd

app = FastAPI(
    title="EcoMonitor Brasil API",
    description="API de indicadores climaticos e sustentabilidade",
    version="3.0.0"
)

BASE = Path(__file__).resolve().parents[1]
ARQUIVO = BASE / "data" / "raw" / "amostra.csv"
NOVOS = BASE / "data" / "processed" / "novos_dados.csv"


class DadosClimaticos(BaseModel):
    cidade: str
    horario: datetime
    temperatura: float
    umidade: float = Field(ge=0, le=100)
    precipitacao: float = Field(ge=0)
    vento: float = Field(ge=0)


@app.get("/")
def inicio():
    return {
        "projeto": "EcoMonitor Brasil",
        "versao": "TP3",
        "status": "API funcionando"
    }


@app.get("/dados")
def consultar_dados():
    tabelas = []

    for arquivo in [ARQUIVO, NOVOS]:
        if arquivo.exists():
            tabelas.append(pd.read_csv(arquivo))

    if not tabelas:
        raise HTTPException(
            status_code=404,
            detail="Dados nao encontrados"
        )

    df = pd.concat(tabelas, ignore_index=True)
    df = df.astype(object).where(pd.notna(df), None)

    return df.to_dict(orient="records")


@app.post("/dados", status_code=201)
def adicionar_dados(dados: DadosClimaticos):
    NOVOS.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame([
        dados.model_dump(mode="json")
    ])

    df.to_csv(
        NOVOS,
        mode="a",
        header=not NOVOS.exists(),
        index=False,
        encoding="utf-8"
    )

    return {
        "mensagem": "Dados adicionados com sucesso",
        "dados": dados
    }
