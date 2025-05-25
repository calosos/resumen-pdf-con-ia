"""
test_procesador_pagina.py

Prueba con integración completa del OCR en el procesamiento de páginas.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PIL import Image, ImageDraw
from extractores.procesador_pagina import ProcesadorPagina
from utils.logger_custom import get_logger
from config import DEBUG_MODE

log = get_logger()

def generar_imagen_con_texto(texto="Diagrama de prueba con OCR"):
    """Crea una imagen blanca con texto negro."""
    imagen = Image.new("RGB", (400, 100), "white")
    draw = ImageDraw.Draw(imagen)
    draw.text((10, 40), texto, fill="black")
    return imagen

def test_procesador_pagina_con_ocr():
    if DEBUG_MODE:
        print("🧪 Iniciando test de ProcesadorPagina con OCR...")

    pagina_mock = {
        "numero_pagina": 7,
        "texto": "Texto base extraído de PDF.",
        "imagenes": [generar_imagen_con_texto()]
    }

    procesador = ProcesadorPagina(idioma_ocr="eng")
    resultado = procesador.procesar_pagina(pagina_mock)

    assert isinstance(resultado, dict), "La salida debe ser un diccionario"
    assert resultado["pagina"] == 7
    assert "contenido" in resultado and isinstance(resultado["contenido"], str)
    assert "ocr_diagramas" in resultado and isinstance(resultado["ocr_diagramas"], list)
    assert any(resultado["ocr_diagramas"]), "El OCR debería haber detectado algo"

    log.ok("Test de ProcesadorPagina con OCR completado con éxito.")
    if DEBUG_MODE:
        print("✅ Test OCR + procesador exitoso.")

if __name__ == "__main__":
    test_procesador_pagina_con_ocr()
