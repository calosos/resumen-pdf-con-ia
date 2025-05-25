"""
logger_custom.py

Logger que guarda en archivo y muestra automáticamente todos los tracebacks en consola.
Colorea solo el prefijo cuando hay print manual.
"""

import logging
from pathlib import Path
from datetime import datetime
from colorama import init, Fore
import sys
import traceback

init(autoreset=True)


class LoggerCustom:
    def __init__(self):
        log_dir = Path(__file__).resolve().parent.parent / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)

        filename = f"resumen_{datetime.now().strftime('%Y%m%d')}.log"
        log_file = log_dir / filename

        self.logger = logging.getLogger("resumen_logger")
        self.logger.setLevel(logging.DEBUG)

        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        formatter = logging.Formatter('[%(asctime)s] %(message)s', datefmt='%Y-%m-%d %H:%M')

        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        self.log_file = log_file

        # Registrar handler global de excepciones no capturadas
        sys.excepthook = self.excepcion_global

    def info(self, mensaje):
        self.logger.info("INFO: " + mensaje)

    def ok(self, mensaje):
        self.logger.info("OK: " + mensaje)

    def advertencia(self, mensaje):
        self.logger.warning("ADVERTENCIA: " + mensaje)

    def error(self, mensaje):
        self.logger.error("ERROR: " + mensaje)
        print(Fore.RED + "ERROR: " + mensaje)

    def excepcion_global(self, tipo, valor, traza):
        traza_str = ''.join(traceback.format_exception(tipo, valor, traza))
        self.logger.error("ERROR (global): " + traza_str)
        print(Fore.RED + traza_str)


# Singleton
_log_instance = None

def get_logger():
    global _log_instance
    if _log_instance is None:
        _log_instance = LoggerCustom()
    return _log_instance
