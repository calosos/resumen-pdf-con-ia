"""
test_ocr_diagramas.py

Prueba unitaria para ocr_diagramas.py usando una imagen generada con texto.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PIL import Image, ImageDraw, ImageFont
from extractores.ocr_diagramas import OCRDiagramas
from utils.logger_custom import get_logger
from config import DEBUG_MODE

log = get_logger()

def generar_imagen_con_texto(texto="Texto OCR de prueba"):
    """Genera una imagen blanca con texto negro."""
    imagen = Image.new("RGB", (400, 100), "white")
    draw = ImageDraw.Draw(imagen)
    try:
        draw.text((10, 40), texto, fill="black")
    except Exception as e:
        log.advertencia(f"No se pudo usar una fuente personalizada: {e}")
        draw.text((10, 40), texto, fill="black")
    return imagen

def test_ocr_diagramas():
    if DEBUG_MODE:
        print("🧪 Iniciando test de OCRDiagramas...")

    imagen_prueba = generar_imagen_con_texto()
    ocr = OCRDiagramas(lang="spa")

    resultado = ocr.aplicar_ocr([imagen_prueba])
    assert isinstance(resultado, list), "La salida debe ser una lista"
    assert len(resultado) == 1, "Debe devolver un solo resultado"
    assert isinstance(resultado[0], str), "El resultado debe ser un string"

    log.ok("Test de OCRDiagramas finalizado correctamente.")
    if DEBUG_MODE:
        print("✅ OCR test finalizado.")

if __name__ == "__main__":
    test_ocr_diagramas()
