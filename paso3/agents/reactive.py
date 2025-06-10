from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from datetime import datetime
import os
import asyncio


model = ChatOllama(model="qwen2.5")

async def main():
    
  server_params = StdioServerParameters(
    command="uv",
    args=["run", "python", os.path.join(os.path.dirname(__file__), "../tools/weather/main.py")],
  )
  
  async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
      await session.initialize()
      tools = await load_mcp_tools(session)
      agent = create_react_agent(model, tools)
      
      now = datetime.now()
      fecha_actual = now.strftime("%-d de %B de %Y")
      hora_actual = now.strftime("%H:%M")
      
      messages = [
        {"role": "system", "content": "Eres un agente que responde preguntas sobre el tiempo."},
        {"role": "system", "content": "Se lo mas escueto posible, respondiendo unicamente con la pregunta del usuario. NO AÑADAS MAS INFORMACIÓN DE LA SOLICITADA, AUNQUE LA TENGAS."},
        {"role": "system", "content": f"Hoy es {fecha_actual}, son las {hora_actual}."},
        {"role": "system", "content": "Estas en Las Rozas de Madrid"},
        {"role": "user", "content": "¿Qué temperatura va a hacer mañana?"}
      ]

      agent_response = None
      async for agent_response in agent.astream({"messages": messages}):
        print(agent_response)
        print("-----------------")

      print("\nRESPUESTA FINAL:\n")
      print(getattr(agent_response["agent"]["messages"][-1], "content", None))

if __name__ == "__main__":
    asyncio.run(main())