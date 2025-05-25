# 🛣️ Roadmap: resumen_pdf_agente

Este archivo documenta las fases del desarrollo y los módulos clave del proyecto, su estado actual y próximas acciones.

---

## ✅ Fase 1: Fundaciones

| Elemento                          | Estado   |
|-----------------------------------|----------|
| `.gitignore`                      | ✅ Listo |
| `requirements.txt`               | ✅ Listo |
| `README.md`                      | ✅ Listo |
| `install_deps.sh` (OCR)         | ✅ Listo |

---

## ✅ Fase 2: Extracción

| Módulo                   | Estado   | Descripción |
|--------------------------|----------|-------------|
| `lector_pdf.py`         | ✅ Listo | Extrae texto e imágenes por página |
| `ocr_diagramas.py`      | ✅ Listo | Aplica OCR a imágenes (con Tesseract) |
| `procesador_pagina.py`  | ✅ Listo | Unifica texto + OCR en una estructura |

---

## ✅ Fase 3: Generación

| Módulo                   | Estado   | Descripción |
|--------------------------|----------|-------------|
| `agente_resumen.py`     | ✅ Listo | Genera resumen por página |
| `agente_diagrama.py`    | ✅ Listo | Interpreta texto OCR de diagramas |

---

## ✅ Fase 4: Salida

| Módulo                        | Estado   | Descripción |
|-------------------------------|----------|-------------|
| `generador_nombres.py`       | ✅ Listo | Nombres tipo Zettelkasten |
| `generador_markdown.py`      | ✅ Listo | Guarda cada resultado en archivo `.md` |

---

## ✅ Fase 5: Orquestación

| Módulo                      | Estado   | Descripción |
|-----------------------------|----------|-------------|
| `controlador_flujo.py`     | ✅ Listo | Orquesta flujo por página |
| `main.py`                  | ✅ Listo | CLI completo: por página y por lote |

---

## 🧪 Fase 6: Pruebas

| Archivo                    | Estado   |
|----------------------------|----------|
| `test_lector_pdf.py`      | ✅ Listo |
| `test_procesador_pagina.py` | ✅ Listo |
| `test_ocr_diagramas.py`   | ✅ Listo |
| `test_agente_resumen.py`  | ✅ Listo |
| `test_agente_diagrama.py` | ✅ Listo |
| `test_generador_nombres.py` | ✅ Listo |
| `test_generador_markdown.py` | ✅ Listo |

---

## 🔜 Próximos pasos sugeridos

- [ ] Mejora del prompt por página con sección de objetivos o contexto
- [ ] Generar MOC o índice general automático
- [ ] Evaluar integración con interfaz web (Flask) o Telegram
- [ ] Añadir conversión opcional `.md` → `.docx` vía Pandoc

