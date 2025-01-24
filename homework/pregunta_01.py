"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd

def pregunta_01():
    """
    Construye y retorna un DataFrame de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requerimientos son los siguientes:

    - El DataFrame debe tener la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minúsculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo espacio
      entre palabra y palabra.

    Retorna:
        pd.DataFrame: El DataFrame con los datos procesados.
    """
    cluster = 'files/input/clusters_report.txt'

    with open(cluster, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    data_lines = lines[4:]

    data = []
    fila_actual = None

    for line in data_lines:
        
        cleaned_line = ' '.join(line.split()).strip()

        if not cleaned_line:
            continue 

        
        if cleaned_line[0].isdigit():
            if fila_actual:
                
                data.append(fila_actual)

            
            parts = cleaned_line.split(maxsplit=3)
            cluster = int(parts[0])
            cantidad = int(parts[1])
            porcentaje = float(parts[2].replace(',', '.').replace('%', ''))
            palabras_clave = parts[3]
            fila_actual = [cluster, cantidad, porcentaje, palabras_clave]
        else:
            
            fila_actual[3] += ' ' + cleaned_line

    
    if fila_actual:
        data.append(fila_actual)

   
    for entry in data:
        
        entry[3] = entry[3].lstrip('%')  
        entry[3] = entry[3].rstrip('.')  
        entry[3] = ' '.join(entry[3].split())  
        
        entry[3] = ', '.join(
            palabra.strip() for palabra in entry[3].split(',') if palabra.strip()
        )

    
    df = pd.DataFrame(
        data,
        columns=[
            "cluster",
            "cantidad_de_palabras_clave",
            "porcentaje_de_palabras_clave",
            "principales_palabras_clave",
        ],
    )

    return df
