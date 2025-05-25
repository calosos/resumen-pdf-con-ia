"""
test_lector_pdf.py

Prueba básica para la clase LectorPDF, con soporte de contraseña opcional.
Usa logger singleton y bandera DEBUG_MODE para imprimir solo si se desea.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extractores.lector_pdf import LectorPDF
from utils.logger_custom import get_logger
from config import DEBUG_MODE

log = get_logger()

def test_lector_pdf():
    ruta_pdf = "entrada_pdf/Curso+Langchain_LLM_Python_protected.pdf"
    password = "langchain_ipd"  # Cambiar si es necesario

    if not os.path.exists(ruta_pdf):
        log.advertencia(f"El archivo de prueba no existe: {ruta_pdf}")
        return

    if DEBUG_MODE:
        print("🔍 Iniciando prueba unitaria de LectorPDF...")

    lector = LectorPDF(ruta_pdf, password=password)
    paginas = lector.leer_pdf_por_pagina()

    assert isinstance(paginas, list), "La salida debe ser una lista"
    assert all("numero_pagina" in p and "texto" in p and "imagenes" in p for p in paginas), "Faltan claves en estructura"

    log.ok(f"Test completado: {len(paginas)} páginas extraídas exitosamente.")

    if DEBUG_MODE:
        print("✅ Test de LectorPDF finalizado correctamente.")

if __name__ == "__main__":
    test_lector_pdf()
