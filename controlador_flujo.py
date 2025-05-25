"""
controlador_flujo.py

Orquesta el flujo de procesamiento de una página PDF:
- extracción
- procesamiento
- resumen
- interpretación de diagramas
- generación de nombre
- guardado en Markdown
"""

from extractores.lector_pdf import LectorPDF
from extractores.procesador_pagina import ProcesadorPagina
from extractores.ocr_diagramas import OCRDiagramas
from agentes.agente_resumen import AgenteResumen
from agentes.agente_diagrama import AgenteDiagrama
from generadores.generador_nombres import GeneradorNombres
from generadores.generador_markdown import GeneradorMarkdown
from utils.logger_custom import get_logger

log = get_logger()

def procesar_pagina_completa(pagina_dict, base_zettelkasten):
    """
    Recibe una página extraída del PDF.
    Ejecuta procesamiento + resumen + interpretación + guardado.
    """
    try:
        numero_pagina = pagina_dict.get("numero_pagina")

        procesador = ProcesadorPagina()
        pagina_procesada = procesador.procesar_pagina(pagina_dict)

        if not pagina_procesada or not pagina_procesada.get("contenido"):
            log.advertencia(f"Pág {numero_pagina} vacía o sin contenido. Se omite.")
            return

        agente_resumen = AgenteResumen()
        resumen_resultado = agente_resumen.generar_resumen(pagina_procesada)

        agente_diagrama = AgenteDiagrama()
        interpretaciones = agente_diagrama.interpretar_diagrama(pagina_procesada.get("ocr_diagramas", []))

        # Nombre de archivo con base y título derivado del resumen
        titulo_referencia = resumen_resultado["resumen"][:50] or f"pagina_{numero_pagina}"
        generador_nombre = GeneradorNombres(base=base_zettelkasten)
        nombre_archivo = generador_nombre.generar_nombre(titulo_referencia)

        generador_md = GeneradorMarkdown()
        generador_md.guardar_md({
            "pagina": numero_pagina,
            "resumen": resumen_resultado["resumen"],
            "interpretaciones": interpretaciones,
            "nombre_archivo": nombre_archivo
        })

    except Exception:
        log.error(f"Error procesando página {pagina_dict.get('numero_pagina', '?')}")
        import traceback
        log.error(traceback.format_exc())
