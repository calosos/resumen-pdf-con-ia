#!/usr/bin/env python3
import os
from pathlib import Path
from dotenv import load_dotenv
from utils.logger_custom import get_logger

log = get_logger()

class GestorEntornoOpenAI:
    def __init__(self, env_filename=".env", nombre_variable="OPENAI_API_KEY", prefijo_valido="sk-"):
        self.env_filename = env_filename
        self.nombre_variable = nombre_variable
        self.prefijo_valido = prefijo_valido
        self.api_key = None

    def cargar_env(self):
        """Carga el archivo .env desde el directorio actual."""
        env_path = Path.cwd() / self.env_filename

        if env_path.exists():
            load_dotenv(dotenv_path=str(env_path), override=True, encoding="utf-8")
            log.ok(".env cargado correctamente (UTF-8).")
            return True

        log.error(f"Archivo {self.env_filename} no encontrado en el directorio actual.")
        self.mostrar_archivos_similares()
        return False

    def mostrar_archivos_similares(self):
        """Busca archivos similares a .env y los imprime si existen."""
        similares = list(Path.cwd().glob("*.env*"))
        if similares:
            log.advertencia("Archivos similares encontrados:")
            for archivo in similares:
                log.info(f" - {archivo.name}")

    def validar_api_key(self):
        """Valida que la API key esté definida, tenga el prefijo correcto y no tenga espacios extra."""
        self.api_key = os.getenv(self.nombre_variable)

        if not self.api_key:
            log.error(f"No se encontró la variable {self.nombre_variable} en el entorno.")
            return False
        if not self.api_key.startswith(self.prefijo_valido):
            log.advertencia(f"La API key no empieza con el prefijo esperado '{self.prefijo_valido}'.")
            return False
        if self.api_key.strip() != self.api_key:
            log.advertencia("La API key tiene espacios al inicio o al final.")
            return False

        log.ok("API key encontrada y válida.")
        return True

    def preparar_entorno(self):
        """Carga el .env y valida la clave. Deja todo listo para usar."""
        log.info("Preparando entorno...")

        if self.cargar_env() and self.validar_api_key():
            log.ok("Entorno y API key listos para usar.")
            return True
        else:
            log.error("Problemas detectados en el entorno o en la API key.")
            return False
