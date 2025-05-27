# generador_nombres.py

import re
import json
import unicodedata
from pathlib import Path
from utils.logger_custom import get_logger

log = get_logger()

class GeneradorNombres:
    def __init__(self, base="15", ruta_contador="contador_nombres.json"):
        """
        base: prefijo numérico del identificador (ej. "15")
        ruta_contador: archivo donde se guarda el progreso del número
        """
        self.prefijo = base
        self.ruta_contador = Path(ruta_contador)
        self.contador = self._cargar_contador()

    def _cargar_contador(self):
        if self.ruta_contador.exists():
            try:
                with open(self.ruta_contador, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get(self.prefijo, 1)  # empieza en 1
            except Exception:
                log.advertencia("No se pudo leer el contador. Reiniciando en 1.")
        return 1

    def _guardar_contador(self):
        data = {}
        if self.ruta_contador.exists():
            try:
                with open(self.ruta_contador, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                log.advertencia("No se pudo leer el contador anterior. Se sobrescribirá.")
        data[self.prefijo] = self.contador
        with open(self.ruta_contador, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def normalizar_texto(self, texto):
        texto_sin_tildes = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
        texto_limpio = re.sub(r'[^\w\s-]', '', texto_sin_tildes).strip().lower()
        texto_guiones = re.sub(r'[\s\-]+', '_', texto_limpio)
        return texto_guiones

    def generar_nombre(self, titulo, sufijo_manual=None):
        """
        Genera un nombre tipo: 15_001_titulo.md, 15_002_titulo.md, ...
        Si se pasa sufijo_manual, lo usa en lugar del número automático.
        """
        try:
            titulo_norm = self.normalizar_texto(titulo)
            sufijo = sufijo_manual if sufijo_manual else f"{self.contador:03d}"  # padding 3 dígitos
            nombre = f"{self.prefijo}_{sufijo}_{titulo_norm}"
            if not sufijo_manual:
                self.contador += 1
                self._guardar_contador()
            log.ok(f"Nombre generado: {nombre}")
            return nombre
        except Exception:
            log.error("Error al generar nombre:")
            import traceback
            log.error(traceback.format_exc())
            return None

    def guardar_archivo_markdown(self, titulo, contenido="", carpeta_salida="salida_markdown"):
        """
        Crea un archivo .md con el nombre generado a partir del título.
        """
        nombre_base = self.generar_nombre(titulo)
        if not nombre_base:
            log.error("No se pudo generar el nombre del archivo.")
            return None

        carpeta = Path(carpeta_salida)
        carpeta.mkdir(parents=True, exist_ok=True)

        ruta_archivo = carpeta / f"{nombre_base}.md"

        try:
            with open(ruta_archivo, "w", encoding="utf-8") as f:
                f.write(f"# {titulo}\n\n{contenido}")
            log.ok(f"Archivo creado: {ruta_archivo}")
            return str(ruta_archivo)
        except Exception:
            log.error("Error al guardar el archivo Markdown:")
            import traceback
            log.error(traceback.format_exc())
            return None
