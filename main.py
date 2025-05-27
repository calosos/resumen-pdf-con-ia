"""
main.py

Punto de entrada completo del proyecto resumen_pdf_agente.
Todo se controla desde aquí: archivo, base Zettelkasten, página, modo debug.
"""

import argparse
from extractores.lector_pdf import LectorPDF
from controlador_flujo import procesar_pagina_completa
from utils.logger_custom import get_logger

log = get_logger()

def ejecutar_en_lote(ruta_pdf, base_zettelkasten, debug=False):
    contrasenia = 'langchain_ipd'
    lector = LectorPDF(ruta_pdf, contrasenia)
    paginas = lector.leer_pdf_por_pagina()

    for pagina_dict in paginas:
        if debug:
            print(f"➡️ Procesando página {pagina_dict['numero_pagina']} con base {base_zettelkasten}...")
        procesar_pagina_completa(pagina_dict, base_zettelkasten)

def ejecutar_una_pagina(ruta_pdf, numero_pagina, base_zettelkasten, debug=False):
    contrasenia = 'langchain_ipd'
    lector = LectorPDF(ruta_pdf, contrasenia)
    paginas = lector.leer_pdf_por_pagina()
    total = len(paginas)

    if numero_pagina < 1 or numero_pagina > total:
        log.error(f"Número de página fuera de rango: 1-{total}")
        return

    pagina_dict = paginas[numero_pagina - 1]
    if debug:
        print(f"➡️ Procesando SOLO la página {numero_pagina} con base {base_zettelkasten}...")
    procesar_pagina_completa(pagina_dict, base_zettelkasten)

def main():
    parser = argparse.ArgumentParser(description="Agente para resumir y describir diagramas de PDFs protegidos.")
    parser.add_argument("--pdf", required=True, help="Ruta al archivo PDF a procesar.")
    parser.add_argument("--base", default="15a", help="Base Zettelkasten para los nombres generados (ej. 15a)")
    parser.add_argument("--pagina", type=int, help="Número de página a procesar (opcional)")
    parser.add_argument("--debug", action="store_true", help="Activa impresión de estado para depuración")

    args = parser.parse_args()

    if args.pagina:
        ejecutar_una_pagina(args.pdf, args.pagina, args.base, debug=args.debug)
    else:
        ejecutar_en_lote(args.pdf, args.base, debug=args.debug)

def mensaje_inicio(texto="\n\t\t\t🚀 Iniciando ejecución del programa..."):
    log.info("\n" + "=" * 100)
    log.info(texto)
    log.info("\n" + "=" * 100 + "\n")
def mensaje_final(texto="\n\t\t\t✅ Proceso finalizado correctamente."):
    log.info("\n" + "=" * 100)
    log.info(texto)
    log.info("\n" + "=" * 100 + "\n")

if __name__ == "__main__":
    mensaje_inicio()
    main()
    mensaje_final()