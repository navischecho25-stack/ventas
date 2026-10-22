import csv
import os
import shutil

archivo_origen = "facturas_hoy.csv"
carpeta_destino = "historial_cartera"
archivo_reporte = "reporte_cartera.txt"

print("--- SISTEMA DE CONTROL DE CARTERA Y COBRANZAS ---")

if os.path.exists(archivo_origen):
    try:
        total_mora = 0
        facturas_pendientes = 0

        with open(archivo_origen, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                # 💡 AQUÍ ESTÁ EL RETO: Queremos filtrar solo las facturas NO pagadas
                # Recuerda que en el CSV, la columna 'pagado' tiene los valores "True" o "False" (como texto).
                
                esta_en_mora = fila["pagado"] == "False"
                monto = int(fila["monto"])

                if esta_en_mora:
                    total_mora += monto
                    facturas_pendientes += 1

        # 1. GENERAR ARCHIVO DE REPORTE
        with open(archivo_reporte, mode="w", encoding="utf-8") as reporte:
            reporte.write("=== REPORTE DE CARTERA PENDIENTE ===\n")
            reporte.write(f"Facturas en mora: {facturas_pendientes}\n")
            reporte.write(f"Total saldo en mora: ${total_mora:,} COP\n")

        print(f"✓ Reporte de cartera generado: '{archivo_reporte}'")

        # 2. MOVER ARCHIVO AL HISTORIAL
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        shutil.move(archivo_origen, os.path.join(carpeta_destino, archivo_origen))
        print(f"✓ Archivo transferido a '{carpeta_destino}'")

    except Exception as error:
        print(f"❌ Error al procesar cartera: {error}")
else:
    print(f"⚠️ El archivo '{archivo_origen}' no fue encontrado.")