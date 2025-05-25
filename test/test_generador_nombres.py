"""
test_generador_nombres.py

Prueba unitaria para el generador de nombres estilo Zettelkasten.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generadores.generador_nombres import GeneradorNombres
from utils.logger_custom import get_logger
from config import DEBUG_MODE

log = get_logger()

def test_generador_nombres():
    if DEBUG_MODE:
        print("🧪 Iniciando test de GeneradorNombres...")

    generador = GeneradorNombres(base="15a")

    ejemplos = [
        ("Introducción a LangChain", "15a_introduccion_a_langchain"),
        ("Qué es un agente?", "15a_que_es_un_agente"),
        ("Carga de documentos 🧾", "15a_carga_de_documentos"),
        ("Módulo 3 - Subtema B", "15a_modulo_3_subtema_b"),
    ]

    for titulo, esperado in ejemplos:
        resultado = generador.generar_nombre(titulo)
        assert resultado == esperado, f"Nombre incorrecto: {resultado} != {esperado}"

    log.ok("Test de GeneradorNombres finalizado correctamente.")
    if DEBUG_MODE:
        print("✅ Test de nombres exitoso.")

if __name__ == "__main__":
    test_generador_nombres()
