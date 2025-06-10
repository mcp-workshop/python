import requests

def get_weather_data(latitude: str, longitud: str) -> str:

  url = f"https://api.open-meteo.com/v1/forecast?daily=weather_code,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,daylight_duration,sunshine_duration,uv_index_max,uv_index_clear_sky_max,rain_sum,showers_sum,snowfall_sum,precipitation_sum,precipitation_hours,precipitation_probability_max,wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant,et0_fao_evapotranspiration,shortwave_radiation_sum&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m,wind_direction_10m,wind_gusts_10m&timezone=Europe%2FBerlin&latitude={latitude}&longitude={longitud}&forecast_days=16"

  response = requests.request(
    "GET",
    url,
    headers={'cache-control': "no-cache"}
  )

  data = response.json()
  return data
