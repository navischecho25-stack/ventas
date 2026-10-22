# Script de Automatización de Control de Cartera 🐍💰

Un script de Python diseñado para la automatización de procesos empresariales (BPA) en pequeñas y medianas empresas (PyMEs).

## 🎯 Propósito
Este script automatiza la gestión diaria de cuentas por cobrar: procesa los datos de cobro, calcula las facturas vencidas, genera un reporte administrativo de resumen y organiza los archivos procesados.

## 🚀 Funcionalidades
- **Filtrado de datos:** Lee archivos CSV entrantes (`facturas_hoy.csv`) para identificar saldos pendientes de pago (`pagado == False`).
- **Cálculos financieros:** Suma la deuda total vencida y cuenta el número de facturas pendientes.
- **Generación de reportes:** Crea un archivo de texto automático con el resumen (`reporte_cartera.txt`).
- **Gestión de archivos:** Mueve de forma segura el archivo CSV procesado a una carpeta de historial (`historial_cartera/`).

## 🛠️ Tecnologías utilizadas
- Python 3
- Módulos nativos: `csv`, `os`, `shutil`