"""
test_agente_diagrama.py

Prueba unitaria para el agente de interpretación de diagramas.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agentes.agente_diagrama import AgenteDiagrama
from utils.logger_custom import get_logger
from config import DEBUG_MODE

log = get_logger()

def test_agente_diagrama():
    if DEBUG_MODE:
        print("🧪 Iniciando test del AgenteDiagrama...")

    textos_ocr = [
        "Entrada -> Proceso A -> Salida",
        """Cliente --- Servidor
    Puerto 443
    HTTPS""",
        "Si x > 10 entonces ejecutar acción Y"
    ]

    agente = AgenteDiagrama()
    resultados = agente.interpretar_diagrama(textos_ocr)

    assert isinstance(resultados, list), "La salida debe ser una lista"
    assert len(resultados) == len(textos_ocr), "Debe haber una interpretación por cada texto"
    assert all(isinstance(r, str) for r in resultados), "Cada interpretación debe ser un string"
    assert any(r.strip() for r in resultados), "Debe haber al menos una interpretación no vacía"

    log.ok("Test de AgenteDiagrama finalizado correctamente.")
    if DEBUG_MODE:
        print("✅ Test de interpretación de diagramas exitoso.")

if __name__ == "__main__":
    test_agente_diagrama()
