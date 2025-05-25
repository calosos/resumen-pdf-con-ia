"""
procesador_pagina.py

Estandariza el contenido de una página PDF para uso con agentes.
Incluye integración con OCR de diagramas.
"""

from utils.logger_custom import get_logger
from extractores.ocr_diagramas import OCRDiagramas
import traceback

log = get_logger()


class ProcesadorPagina:
    def __init__(self, idioma_ocr="eng"):
        self.ocr = OCRDiagramas(lang=idioma_ocr)

    def procesar_pagina(self, pagina_dict):
        """
        Recibe un diccionario con:
        - numero_pagina
        - texto
        - imagenes (lista de PIL.Image)

        Retorna un nuevo diccionario estandarizado:
        {
            "pagina": int,
            "contenido": str,
            "imagenes": list,
            "ocr_diagramas": list
        }
        """
        try:
            pagina = pagina_dict.get("numero_pagina")
            texto = pagina_dict.get("texto", "")
            imagenes = pagina_dict.get("imagenes", [])

            log.info(f"Procesando página {pagina}...")

            # Aplicar OCR a los diagramas
            textos_ocr = self.ocr.aplicar_ocr(imagenes)

            # Unificar texto extraído del PDF con el OCR (solo si hay contenido)
            contenido_unificado = texto.strip()
            if any(textos_ocr):
                contenido_unificado += "\n\n" + "\n".join(
                    [t for t in textos_ocr if t]
                )

            resultado = {
                "pagina": pagina,
                "contenido": contenido_unificado,
                "imagenes": imagenes,
                "ocr_diagramas": textos_ocr
            }

            log.ok(f"Página {pagina} procesada y estandarizada.")
            return resultado

        except Exception:
            log.error(f"Error al procesar la página {pagina_dict.get('numero_pagina', '?')}:")
            log.error(traceback.format_exc())
            return None
