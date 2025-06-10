from langchain_ollama import ChatOllama

model = ChatOllama(model="qwen2.5")

async def main():
    response = await model.ainvoke("¿Como te llamas? ¿Qué tal estás?")
    print(response.content)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
