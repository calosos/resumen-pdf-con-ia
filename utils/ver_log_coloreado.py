"""
ver_log_coloreado.py

Muestra el log del día actual coloreando la fecha y el prefijo.
- Fecha en azul
- OK en verde
- ERROR en rojo
- INFO en cian
- ADVERTENCIA en amarillo
"""

import time
from colorama import init, Fore, Style
from datetime import datetime
from pathlib import Path
import re

init(autoreset=True)

def colorear_prefijo_y_fecha(linea):
    # Fecha entre corchetes al inicio
    fecha_match = re.match(r"(\[.*?\])", linea)
    if fecha_match:
        fecha_coloreada = Fore.BLUE + fecha_match.group(1) + Style.RESET_ALL
        linea = fecha_coloreada + linea[fecha_match.end():]

    # Prefijos
    prefijos_colores = {
        "ERROR:": Fore.RED,
        "ADVERTENCIA:": Fore.YELLOW,
        "OK:": Fore.GREEN,
        "INFO:": Fore.CYAN
    }

    for prefijo, color in prefijos_colores.items():
        if prefijo in linea:
            partes = linea.split(prefijo, 1)
            return partes[0] + color + prefijo + Style.RESET_ALL + partes[1]

    return linea

def seguir_log_coloreado(log_path):
    if not log_path.exists():
        print(f"ERROR: El archivo no existe -> {log_path}")
        return

    with log_path.open("r", encoding="utf-8", errors="ignore") as f:
        f.seek(0, 2)  # ir al final
        print(f"INFO: Monitoreando {log_path} en tiempo real...\nPresiona Ctrl+C para salir.")
        try:
            while True:
                linea = f.readline()
                if not linea:
                    time.sleep(0.2)
                    continue
                print(colorear_prefijo_y_fecha(linea.rstrip()))
        except KeyboardInterrupt:
            print("\nINFO: Finalizado por el usuario.")

if __name__ == "__main__":
    nombre_log = f"resumen_{datetime.now().strftime('%Y%m%d')}.log"
    ruta_log = Path("logs") / nombre_log
    seguir_log_coloreado(ruta_log)
