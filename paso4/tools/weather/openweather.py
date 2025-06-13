import requests

def get_weather_data(latitude: str, longitude: str) -> str:

  url = f"https://api.open-meteo.com/v1/forecast?daily=precipitation_probability_max,wind_speed_10m_max,uv_index_max,temperature_2m_min,temperature_2m_max,rain_sum&timezone=Europe%2FBerlin&latitude={latitude}&longitude={longitude}"

  response = requests.request(
    "GET",
    url,
    headers={'cache-control': "no-cache"}
  )

  data = response.json()
  return data
