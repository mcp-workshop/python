from mcp.server.fastmcp import FastMCP
from google import get_travel_time, get_coordinates_from_address, get_address_from_coordinates

mcp = FastMCP("Weather MCP Server")

@mcp.tool()
def calculate_route(origin: str = "real, 2, las rozas", destination: str = "via de los poblados 1, madrid", travel_mode: str = "driving", arrival_time: str = None) -> dict:
  """
  Calcula la ruta y duración entre dos puntos usando Google Maps. 
  Parámetros: origin y destination como direcciones.
  Modos de transporte: driving, walking, bicycling, or transit.
  arrival_time es opcional y debe ser una cadena de texto con el formato epoch time.
  resultado es un diccionario con la duración del viaje en texto, en segundos y las direcciones de origen y destino.
  """
  return get_travel_time(origin, destination, travel_mode, arrival_time)

@mcp.tool()
def get_coordinates(address: str) -> tuple:
  """
  Obtiene las coordenadas de una dirección.
  """
  return get_coordinates_from_address(address)

@mcp.tool()
def get_address(coordinates: tuple) -> str:
  """
  Obtiene la dirección a partir de las coordenadas.
  """
  return get_address_from_coordinates(*coordinates)
  
if __name__ == "__main__":
  mcp.run()