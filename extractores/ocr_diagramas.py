"""
ocr_diagramas.py

Aplica OCR a una lista de imágenes usando pytesseract.
Devuelve una lista de strings con el texto extraído.
"""

from PIL import Image
import pytesseract
import traceback
from utils.logger_custom import get_logger

class OCRDiagramas:
    def __init__(self, lang="eng"):
        """
        lang: idioma OCR (por ejemplo, 'eng' o 'spa')
        """
        self.lang = lang
        self.log = get_logger()

    def aplicar_ocr(self, lista_imagenes):
        """
        Aplica OCR a cada imagen en la lista.
        Retorna una lista de strings.
        """
        resultados = []

        if not lista_imagenes:
            self.log.advertencia("Lista de imágenes vacía. No se aplicó OCR.")
            return resultados

        for idx, imagen in enumerate(lista_imagenes):
            try:
                if not isinstance(imagen, Image.Image):
                    self.log.advertencia(f"Elemento {idx+1} no es una instancia válida de PIL.Image. Se omite.")
                    resultados.append("")
                    continue

                texto = pytesseract.image_to_string(imagen, lang=self.lang).strip()
                resultados.append(texto)

                if texto:
                    self.log.ok(f"OCR aplicado con éxito a imagen {idx+1}.")
                else:
                    self.log.advertencia(f"OCR no encontró texto en imagen {idx+1}.")

            except Exception:
                self.log.error(f"Error al aplicar OCR en imagen {idx+1}:")
                self.log.error(traceback.format_exc())
                resultados.append("")

        return resultados
