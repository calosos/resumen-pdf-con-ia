"""
test_agente_resumen.py

Prueba unitaria para el agente de resumen con contenido simulado.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agentes.agente_resumen import AgenteResumen
from utils.logger_custom import get_logger
from config import DEBUG_MODE

log = get_logger()

def test_agente_resumen():
    if DEBUG_MODE:
        print("🧪 Iniciando test del AgenteResumen...")

    contenido_simulado = {
        "pagina": 1,
        "contenido": (
            "LangChain es un framework que facilita la construcción de aplicaciones LLM. "
            "Permite encadenar múltiples llamadas a modelos, integrarse con fuentes externas, "
            "y crear agentes que razonan sobre herramientas. Este documento presenta su uso básico, "
            "componentes clave y casos de aplicación con OpenAI y Python."
        )
    }

    agente = AgenteResumen()
    resultado = agente.generar_resumen(contenido_simulado)

    assert isinstance(resultado, dict), "La salida debe ser un diccionario"
    assert "pagina" in resultado and resultado["pagina"] == 1
    assert "resumen" in resultado and isinstance(resultado["resumen"], str)
    assert len(resultado["resumen"]) > 0, "El resumen no debe estar vacío"

    log.ok("Test de AgenteResumen finalizado correctamente.")
    if DEBUG_MODE:
        print("✅ Test de resumen exitoso.")

if __name__ == "__main__":
    test_agente_resumen()
