from mcp.server.fastmcp import FastMCP
from cal_loader import get_calendar_events

mcp = FastMCP("Weather MCP Server")

@mcp.tool()
def load_calendar_events() -> dict:
    """
    Carga todos los eventos de un calendario CalDAV (.ics) desde una URL definida en .env.
    """
    return get_calendar_events()

if __name__ == "__main__":
    mcp.run()
