# 📚 Proyecto: resumen_pdf_agente

Este proyecto implementa un **agente inteligente en Python** que procesa archivos PDF con diagramas y texto, y genera un resumen por página. El resumen se guarda en archivos Markdown (`.md`) con nombres tipo Zettelkasten.

---

## 🚀 Características principales

- Procesa archivos PDF protegidos o no protegidos
- Extrae texto y diagramas por página
- Aplica OCR sobre imágenes de cada página
- Usa LLMs (GPT-4o, GPT-4o-mini) para:
  - Resumir el contenido
  - Interpretar texto extraído de diagramas
- Genera archivos `.md` con formato estructurado
- Cada archivo tiene nombre Zettelkasten (`15a_Titulo_Tema.md`)
- Logging a color en consola y archivo
- Totalmente modular, extensible y CLI-friendly

---

## ⚙️ Instalación

1. Clona el repositorio y entra al proyecto:

```bash
git clone <url>
cd resumen_pdf_agente
```

2. Crea un entorno virtual:

```bash
python -m venv env
source env/bin/activate  # o env\Scripts\activate en Windows
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Asegúrate de tener instalado Tesseract OCR y que esté en tu PATH.

---

## 🔐 Configuración

Crea un archivo `.env` en la raíz del proyecto con tu clave de OpenAI:

```
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## 🧪 Uso desde terminal

### Procesar todo el PDF:

```bash
python main.py --pdf entrada_pdf/Curso+Langchain_LLM_Python_protected.pdf --base 15a
```

### Procesar una sola página:

```bash
python main.py --pdf entrada_pdf/Curso+Langchain_LLM_Python_protected.pdf --pagina 3 --base 15a
```

### Activar debug (print adicionales):

```bash
python main.py --pdf entrada_pdf/Curso+Langchain_LLM_Python_protected.pdf --debug
```

---

## 🧱 Estructura del proyecto

```bash
resumen_pdf_agente/
├── main.py
├── config.py
├── gestor_entorno_openai.py
├── controlador_flujo.py
│
├── agentes/
│   ├── agente_resumen.py
│   └── agente_diagrama.py
├── extractores/
│   ├── lector_pdf.py
│   ├── ocr_diagramas.py
│   └── procesador_pagina.py
├── generadores/
│   ├── generador_nombres.py
│   └── generador_markdown.py
├── utils/
│   ├── logger_custom.py
│   └── ver_log_coloreado.py
│
├── entrada_pdf/
├── salida_markdown/
├── logs/
├── test/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧩 Créditos

Desarrollado por [Carlos Ortíz Suárez] para organizar conocimiento extraído de documentos con IA.

