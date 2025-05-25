"""
generador_markdown.py

Genera y guarda un archivo .md con el resumen e interpretaciones de una página PDF.
"""

from pathlib import Path
from utils.logger_custom import get_logger
from config import BASE_DIR, ENCODING

log = get_logger()

class GeneradorMarkdown:
    def __init__(self, carpeta_salida=None):
        self.carpeta = carpeta_salida or BASE_DIR / "salida_markdown"
        self.carpeta.mkdir(parents=True, exist_ok=True)

    def guardar_md(self, datos_pagina):
        """
        datos_pagina: dict con claves esperadas:
        - 'pagina': int
        - 'resumen': str
        - 'interpretaciones': list[str] (opcional)
        - 'nombre_archivo': str (sin extensión)

        Crea un archivo .md con el contenido formateado.
        """
        try:
            pagina = datos_pagina.get("pagina", "?")
            resumen = datos_pagina.get("resumen", "").strip()
            interpretaciones = datos_pagina.get("interpretaciones", [])
            nombre_archivo = datos_pagina.get("nombre_archivo", f"pagina_{pagina}").strip()

            if not resumen and not interpretaciones:
                log.advertencia(f"No hay contenido para guardar en página {pagina}.")
                return None

            path_salida = self.carpeta / f"{nombre_archivo}.md"

            with open(path_salida, "w", encoding=ENCODING) as f:
                f.write(f"# 🧩 Resumen página {pagina}\n\n")
                if resumen:
                    f.write("## 📘 Resumen generado\n\n")
                    f.write(resumen + "\n\n")
                if interpretaciones:
                    f.write("## 🖼️ Interpretaciones de diagramas\n\n")
                    for idx, texto in enumerate(interpretaciones, 1):
                        f.write(f"**Diagrama {idx}:**\n{texto}\n\n")

            log.ok(f"Archivo .md guardado: {path_salida.name}")
            return str(path_salida)

        except Exception:
            log.error("Error al guardar archivo Markdown:")
            import traceback
            log.error(traceback.format_exc())
            return None
