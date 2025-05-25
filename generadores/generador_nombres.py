"""
generador_nombres.py

Genera nombres de archivo tipo Zettelkasten a partir de una base numérica y texto.
"""

import re
import unicodedata
from utils.logger_custom import get_logger

log = get_logger()

class GeneradorNombres:
    def __init__(self, base="15"):
        """
        base: identificador numérico inicial del archivo (ej. "15", "15a", "3c1")
        """
        self.base = base

    def normalizar_texto(self, texto):
        """
        Limpia y normaliza un texto para usarlo como parte del nombre de archivo:
        - sin tildes ni caracteres especiales
        - reemplaza espacios por guiones bajos
        - solo letras, números y guiones bajos
        """
        texto_sin_tildes = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
        texto_limpio = re.sub(r'[^\w\s-]', '', texto_sin_tildes).strip().lower()
        texto_guiones = re.sub(r'[\s\-]+', '_', texto_limpio)
        return texto_guiones

    def generar_nombre(self, titulo, sufijo=None):
        """
        Genera un nombre tipo Zettelkasten:
        base + "_" + titulo_normalizado

        Ejemplo:
        entrada: base="15c", titulo="Conectores en LangChain"
        salida: 15c_conectores_en_langchain

        Puedes pasar sufijo extra (opcional)
        """
        try:
            titulo_norm = self.normalizar_texto(titulo)
            nombre = f"{self.base}_{titulo_norm}"
            if sufijo:
                nombre += f"_{self.normalizar_texto(sufijo)}"

            log.ok(f"Nombre generado: {nombre}")
            return nombre
        except Exception:
            log.error("Error al generar nombre:")
            import traceback
            log.error(traceback.format_exc())
            return None
