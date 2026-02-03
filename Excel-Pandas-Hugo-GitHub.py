import pandas as pd
import os

def generar_contenido():
    # Asegúrate de tener instalado: pip install pandas openpyxl
    df = pd.read_excel("automation/datos_origen.xlsx", sheet_name='Equipos')
    
    for _, row in df.iterrows():
        # Carpeta según tipo
        folder = f"content/{row['Tipo'].lower()}"
        os.makedirs(folder, exist_ok=True)
        
        filename = f"{folder}/{row['ID']}.md"
        
        # Lógica del botón de factura
        boton_factura = ""
        if row['Tipo'].lower() == 'factura':
            boton_factura = f"{{{{< button href=\"{row['URL_Cotizacion']}\" >}}}}Descargar Factura PDF{{{{< /button >}}}}"

        content = f"""---
title: "{row['Nombre']}"
date: {row['Fecha']}
image: "/images/{row['Imagen']}"
price: "{row['Precio']}"
---
![{row['Nombre']}]({row['Imagen']})

### Detalles del Registro
- **Modelo:** {row['Modelo']}
- **Costo:** {row['Precio']} USD

{boton_factura}
"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    print("✅ Archivos generados correctamente.")

if __name__ == "__main__":
    generar_contenido()