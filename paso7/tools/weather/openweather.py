import os
import requests
from dotenv import load_dotenv

def get_weather_data(latitude: str, longitud: str) -> str:
  load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

  url = f"https://api.open-meteo.com/v1/forecast?daily=precipitation_probability_max,wind_speed_10m_max,uv_index_max,temperature_2m_min,temperature_2m_max,rain_sum&timezone=Europe%2FBerlin&latitude={latitude}&longitude={longitud}"

  response = requests.request(
    "GET",
    url,
    headers={'cache-control': "no-cache"}
  )

  data = response.json()
  return data
