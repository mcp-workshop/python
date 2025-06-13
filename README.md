

# taller de agentes y mcp
## Uso con Dev Container

Este proyecto está preparado para funcionar en un **Dev Container** de VS Code. Un Dev Container es un entorno de desarrollo preconfigurado y reproducible que incluye todas las dependencias necesarias (como Python y node) dentro de un contenedor Docker.

### ¿Qué ventajas tiene?

- No necesitas instalar nada en tu máquina salvo Docker y Visual Studio Code.
- El entorno es idéntico para todos los usuarios.
- Incluye todas las herramientas necesarias (Python, node, git, etc.) ya instaladas.

### ¿Cómo usar el proyecto con Dev Container?

1. Instala [Docker](https://docs.docker.com/get-docker/) y [Visual Studio Code](https://code.visualstudio.com/).
2. Instala la extensión [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) en VS Code.
3. Abre este proyecto en VS Code.
4. Cuando VS Code lo detecte, selecciona **"Reopen in Container"** o abre la paleta de comandos (`Ctrl+Shift+P` en windows y linux o `Cmd+Shift+p` en mac), busca `Dev Containers: Reopen in Container` y ejecútalo.
5. Espera a que se construya el contenedor (esto puede tardar varios minutos la primera vez, se descarga la imagen e instala las dependencias).
6. ¡Listo! Ya puedes usar el entorno con todas las dependencias instaladas.

> Si necesitas reconstruir el contenedor (por ejemplo, tras cambiar el Dockerfile), usa la opción **"Dev Containers: Rebuild and Reopen in Container"** desde la paleta de comandos.

Este proyecto usa [Model Context Protocol](https://github.com/modelcontextprotocol/python-sdk), LangGraph y LangChain.

## Conexión a ollama

El dev container se levanta en la misma red que el host y hacer fordward del puerto de ollama por defecto, el 11434. Si cambiarais esto, debeis cambiar tanto el forwardPorts como la variable de entorno OLLAMA_API_URL.

## Variables de entorno

He quitado los .env, mania mia, y he movida las variables a la configuración del dev container. Si quereis usar langfuse, cambiar el ics del calendario, o usar google maps, tendresi que actualizar las variables de entorno en la configuracion del devcontainer: `.devcontainer/devcontainer.json` y hacer un rebuild del contenedor: abre la paleta de comandos (`Ctrl+Shift+P` en windows y linux o `Cmd+Shift+p` en mac), busca `Dev Containers: Rebuild Container` y ejecútalo.

## Instalación

El dev container instala las dependencias python despues de crearse y cada vez que se hace un rebuild, pero siempre se puede hacer a mano normalmente:

```bash
pip install .
```

## tools

En la carpeta `tools` están las siguientes herramientas (todas usan el [SDK oficial de Model Context Protocol](https://github.com/modelcontextprotocol/python-sdk)):

- **calendar**: herramienta que permite consultar eventos de un calendario en formato iCal.
- **weather**: herramienta que obtiene información meteorológica actual y pronósticos.
- **drive**: herramienta que te prevision de tiempo de viaje con google maps, coordenadas y direcciones.

> **Nota:** La herramienta **calendar** funciona como un servidor SSE (Server-Sent Events), por lo que debe estar en ejecución antes de que los agentes puedan consultarla. Para iniciar el servidor de calendar, ejecuta:

```bash
python pasoX/tools/calendar/main.py
```

Asegúrate de que este proceso esté activo antes de lanzar cualquier agente que dependa de la herramienta de calendario.

## agents

se encuentran los agentes inteligentes implementados. Cada agente está diseñado para interactuar con una o varias herramientas MCP, resolviendo tareas específicas mediante flujos definidos con LangGraph o LangChain. Consulta la documentación de cada agente para detalles sobre su funcionamiento y configuración.

## Ejecución

Para ejecutar un agente, por ejemplo el reactivo:

```bash
python pasoX/agents/reactive.py
```

## listado de actividades a las que corresponde cada paso:

🛠️ **Actividad paso0**: Clonar proyecto base y ejecutar un ejemplo simple en cada lenguaje

python test_ollama.py

🛠️ **Actividad paso1**: Añadir una función que devuelva la respuesta de open meteo completa

python paso1/tools/weather/main.py

🛠️ **Actividad paso2**: Añadir una herramienta que use la función anterior

npx @modelcontextprotocol/inspector (python paso2/tools/weather/main.py)

🛠️ **Actividad paso3**: Creamos un agente react, que es el más sencillo de desarrollar, y que llame a la herramienta anterior.

python paso3/agents/reactive.py

🛠️ **Actividad paso4**: Vamos a hacer una poda a la respuesta de open meteo. ¿Mejoran las respuestas? ¿Y el tiempo de ejecución?

python paso4/agents/reactive.py

🛠️ **Actividad paso5**: Añadir una función que llame a un calendario ICS y devuelva un JSON con tus eventos

python paso5/tools/calendar/main.py
npx @modelcontextprotocol/inspector (http://127.0.0.1:8000/sse)

🛠️ **Actividad paso6**: Haz que tu agente use las dos herramientas en una sola consulta

python paso6/tools/calendar/main.py
python paso6/agents/reactive.py

🛠️ **Demo paso7**: Uso de LangFuse

docker compose up -d (ejecutarlo en el ordenador, no en el dev container)
python paso7/agents/reactive.py

🛠️ **Demo pasoGdrive**: Bonus track + google drive WIP

docker compose up -d (ejecutarlo en el ordenador, no en el dev container)
python pasoGdrive/agents/reactive.py
