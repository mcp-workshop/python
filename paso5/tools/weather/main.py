from mcp.server.fastmcp import FastMCP
from openweather import get_weather_data

mcp = FastMCP("Weather MCP Server")

@mcp.tool()
def load_weather_data(latitude: str = "40.477623", longitud: str = "-3.6373624") -> dict:
    """
    Carga los datos del clima desde open Weather API, la longitud y latitud especificadas.
    """
    return get_weather_data(latitude, longitud)

if __name__ == "__main__":
    mcp.run()
