"""
agente_resumen.py

Agente LangChain que genera un resumen del contenido procesado de una página.
"""

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from config import OPENAI_API_KEY, MODELO_OPENAI
from utils.logger_custom import get_logger
import traceback

log = get_logger()

class AgenteResumen:
    def __init__(self):
        try:
            self.llm = ChatOpenAI(
                openai_api_key=OPENAI_API_KEY,
                model_name=MODELO_OPENAI,
                temperature=0.3,
                max_tokens=1100
            )
            self.prompt = PromptTemplate(
                input_variables=["contenido"],
                template="""
Actúa como un asistente experto en gestión del conocimiento. Quiero que transformes el siguiente texto en una nota **conceptual**, escrita en un formato claro y útil para repaso en Obsidian.

Aplica las siguientes reglas:
 
1. Resume con lenguaje neutro, sin tono personal ni institucional.
 2. Destaca los **conceptos clave** y su aplicación práctica.
 3. Utiliza encabezados en estilo Markdown (`#`, `##`) para estructurar la nota.
 4. Omite frases promocionales, redundancias y llamadas a la acción innecesarias.
Contenido:
{contenido}

Resumen:
"""
            )
        except Exception:
            log.error("Error al inicializar el agente de resumen:")
            log.error(traceback.format_exc())

    def generar_resumen(self, datos_pagina):
        """
        Espera un dict con: {'pagina': int, 'contenido': str}
        Devuelve un dict con: {'pagina': int, 'resumen': str}
        """
        try:
            contenido = datos_pagina.get("contenido", "")
            pagina = datos_pagina.get("pagina", "?")

            if not contenido.strip():
                log.advertencia(f"Pág {pagina} sin contenido útil. Se omite resumen.")
                return {"pagina": pagina, "resumen": ""}

            log.info(f"Generando resumen para página {pagina}...")

            chain = self.prompt | self.llm
            respuesta = chain.invoke({"contenido": contenido})
            texto_resumen = respuesta.content.strip()

            log.ok(f"Resumen generado para página {pagina}.")
            return {"pagina": pagina, "resumen": texto_resumen}

        except Exception:
            log.error(f"Error al generar resumen para página {datos_pagina.get('pagina', '?')}:")
            log.error(traceback.format_exc())
            return {"pagina": datos_pagina.get("pagina", "?"), "resumen": ""}
