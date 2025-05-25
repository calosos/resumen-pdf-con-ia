"""
agente_diagrama.py

Agente LangChain que interpreta el texto extraído por OCR de diagramas.
Genera descripciones o inferencias útiles a partir de ellos.
"""

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from config import OPENAI_API_KEY, MODELO_OPENAI
from utils.logger_custom import get_logger
import traceback

log = get_logger()

class AgenteDiagrama:
    def __init__(self):
        try:
            self.llm = ChatOpenAI(
                openai_api_key=OPENAI_API_KEY,
                model_name=MODELO_OPENAI,
                temperature=0.3,
                max_tokens=500
            )
            self.prompt = PromptTemplate(
                input_variables=["ocr_texto"],
                template="""
Eres un asistente que ayuda a interpretar texto técnico extraído de diagramas o imágenes.

Dado el siguiente contenido OCR extraído de un diagrama, interpreta su posible significado o describe lo que representa, siempre con tono informativo y claro.

OCR extraído:
{ocr_texto}

Interpretación:
"""
            )
        except Exception:
            log.error("Error al inicializar el agente de diagramas:")
            log.error(traceback.format_exc())

    def interpretar_diagrama(self, lista_textos_ocr):
        """
        Recibe una lista de textos (uno por imagen procesada).
        Devuelve una lista con interpretaciones correspondientes.
        """
        resultados = []
        try:
            if not lista_textos_ocr:
                log.advertencia("Lista vacía de textos OCR. No hay diagramas para interpretar.")
                return resultados

            chain = self.prompt | self.llm

            for idx, texto in enumerate(lista_textos_ocr):
                if not texto.strip():
                    log.advertencia(f"Imagen {idx+1} sin texto útil para interpretar.")
                    resultados.append("")
                    continue

                log.info(f"Interpretando contenido de imagen {idx+1}...")
                respuesta = chain.invoke({"ocr_texto": texto})
                resultados.append(respuesta.content.strip())
                log.ok(f"Interpretación generada para imagen {idx+1}.")

        except Exception:
            log.error("Error en la interpretación de diagramas:")
            log.error(traceback.format_exc())

        return resultados
