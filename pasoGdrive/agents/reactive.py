from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from datetime import datetime
from langfuse.langchain import CallbackHandler
from dotenv import load_dotenv
import uuid
import os
import asyncio

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

handler: CallbackHandler = CallbackHandler()

model = ChatOllama(model="qwen2.5")

async def main():  
  client = MultiServerMCPClient(
    {
      "weather": {
        "command": "uv",
        "args": ["run", "python", os.path.join(os.path.dirname(__file__), "../tools/weather/main.py")],
        "transport": "stdio",
      },
      "calendar": {
        "command": "uv",
        "args": ["run", "python", os.path.join(os.path.dirname(__file__), "../tools/calendar/main.py")],
        "transport": "stdio",
      },
      "drive": {
        "command": "uv",
        "args": ["run", "python", os.path.join(os.path.dirname(__file__), "../tools/drive/main.py")],
        "transport": "stdio",
      },
    }
  )
  
  tools = await client.get_tools()
  
  agent = create_react_agent(model, tools)
  
  now = datetime.now()
  fecha_actual = now.strftime("%-d de %B de %Y")
  hora_actual = now.strftime("%H:%M")

  messages = [
    {"role": "system", "content": "Eres un agente que responde preguntas. Tienes acceso a herramientas de calendario, meteorología y de Google Maps para calcualr tiempos de viaje."},
    {"role": "system", "content": "Se lo mas escueto posible, respondiendo unicamente con la pregunta del usuario. NO AÑADAS MAS INFORMACIÓN DE LA SOLICITADA, AUNQUE LA TENGAS."},
    {"role": "system", "content": f"Hoy es {fecha_actual}, son las {hora_actual}."},
    {"role": "system", "content": "Si no sabes cuando es un evento, busca en la herramienta de calendario."},
    {"role": "system", "content": "Si no se especifica donde esta el usuario, asume que esta en Las Rozas de Madrid."},
    {"role": "user", "content": "¿para la Weekly GenAI, a que hora deberia salir de casa?"},
  ]
  agent_response = None
  async for agent_response in agent.astream({"messages": messages, }, config={"callbacks": [handler]}):
    print(agent_response)
    print("-----------------")
  
  print("\nRESPUESTA FINAL:\n")
  print(getattr(agent_response["agent"]["messages"][-1], "content", None))

if __name__ == "__main__":
  asyncio.run(main())