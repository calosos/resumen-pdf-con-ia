"""
test_generador_markdown.py

Prueba unitaria del generador_markdown.py con entrada simulada.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generadores.generador_markdown import GeneradorMarkdown
from utils.logger_custom import get_logger
from config import DEBUG_MODE

log = get_logger()

def test_generador_markdown():
    if DEBUG_MODE:
        print("🧪 Iniciando test de GeneradorMarkdown...")

    entrada_simulada = {
        "pagina": 3,
        "resumen": "Este es un resumen de prueba sobre el contenido de la página 3.",
        "interpretaciones": [
            "Este diagrama representa el flujo de datos entre cliente y servidor.",
            "Este esquema muestra una condición lógica evaluada en un sistema de decisiones."
        ],
        "nombre_archivo": "15c3_Ejemplo_Resumen_Pagina"
    }

    generador = GeneradorMarkdown()
    resultado = generador.guardar_md(entrada_simulada)

    assert resultado and resultado.endswith(".md"), "El resultado debe ser una ruta a un archivo .md"
    assert os.path.exists(resultado), "El archivo .md debe existir en el sistema"

    log.ok("Test de GeneradorMarkdown finalizado correctamente.")
    if DEBUG_MODE:
        print("✅ Markdown generado con éxito.")

if __name__ == "__main__":
    test_generador_markdown()
