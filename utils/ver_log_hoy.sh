#!/bin/bash

echo "INFO: Activando entorno virtual..."
source env/bin/activate

echo "INFO: Ejecutando visor de log en tiempo real para el día actual..."
python utils/ver_log_coloreado.py

echo "INFO: Cerrando entorno virtual..."
deactivate
