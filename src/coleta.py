import requests
import pandas as pd

def coletar():
    r = requests.get("https://api.open-meteo.com/v1/forecast", params={"latitude": -23.55, "longitude": -46.63, "hourly": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m", "timezone": "America/Sao_Paulo", "forecast_days": 1}, timeout=15)
    r.raise_for_status()
    h = r.json()["hourly"]
    return pd.DataFrame({"cidade": "São Paulo", "horario": h["time"], "temperatura": h["temperature_2m"], "umidade": h["relative_humidity_2m"], "precipitacao": h["precipitation"], "vento": h["wind_speed_10m"]})
