"""
lector_pdf.py

Extrae texto e imágenes por página desde un PDF, con opción de contraseña.
Incluye logging con singleton y manejo explícito de errores por contraseña.
"""

import pdfplumber
from PIL import Image
from io import BytesIO
import traceback
from pdfplumber.utils.exceptions import PdfminerException
from utils.logger_custom import get_logger

log = get_logger()

class LectorPDF:
    def __init__(self, ruta_pdf, password=None):
        self.ruta_pdf = ruta_pdf
        self.password = password

    def leer_pdf_por_pagina(self):
        paginas_extraidas = []

        try:
            try:
                pdf = pdfplumber.open(self.ruta_pdf, password=self.password)
            except PdfminerException as e:
                log.error("ERROR: El PDF está protegido con contraseña incorrecta o no se puede abrir.")
                log.error(str(e))
                return []

            with pdf:
                log.info(f"Archivo PDF abierto correctamente: {self.ruta_pdf}")
                total_paginas = len(pdf.pages)
                log.info(f"Total de páginas: {total_paginas}")

                for i, pagina in enumerate(pdf.pages, start=1):
                    texto = pagina.extract_text() or ""
                    imagenes = []

                    for img_dict in pagina.images:
                        try:
                            im = pagina.to_image(resolution=300)
                            bbox = (img_dict["x0"], img_dict["top"], img_dict["x1"], img_dict["bottom"])
                            recorte = im.original.crop(bbox)
                            imagenes.append(recorte)
                        except Exception as e:
                            log.advertencia(f"No se pudo extraer imagen en página {i}: {e}")

                    paginas_extraidas.append({
                        "numero_pagina": i,
                        "texto": texto.strip(),
                        "imagenes": imagenes
                    })

                    log.ok(f"Página {i} procesada correctamente.")

        except Exception:
            log.error("Error inesperado al procesar el PDF:")
            log.error(traceback.format_exc())

        return paginas_extraidas
