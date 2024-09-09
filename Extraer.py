import requests
import pandas as pd

# Lista de URLs de las páginas web con tablas
urls = [
    "https://es.numbeo.com/coste-de-vida/clasificaciones-por-país?title=2024",
    "https://es.numbeo.com/coste-de-vida/clasificaciones-por-país?title=2023",
    "https://es.numbeo.com/coste-de-vida/clasificaciones-por-país?title=2022",
    "https://es.numbeo.com/coste-de-vida/clasificaciones-por-país?title=2021",
    "https://es.numbeo.com/coste-de-vida/clasificaciones-por-país?title=2020",
    "https://es.numbeo.com/coste-de-vida/clasificaciones-por-país?title=2019",
    "https://es.numbeo.com/coste-de-vida/clasificaciones-por-país?title=2018",
    "https://es.numbeo.com/coste-de-vida/clasificaciones-por-país?title=2017",
    "https://es.numbeo.com/coste-de-vida/clasificaciones-por-país?title=2016",
    "https://es.numbeo.com/coste-de-vida/clasificaciones-por-país?title=2015",
    "https://es.numbeo.com/coste-de-vida/clasificaciones-por-país?title=2014"
]

# Iterar sobre la lista de URLs
for i, url in enumerate(urls):
    try:
        # Realizar la solicitud HTTP usando requests
        response = requests.get(url)

        # Especificar la codificación (UTF-8)
        response.encoding = 'utf-8'

        # Leer todas las tablas de la página web
        tables = pd.read_html(response.text)

        # Iterar sobre todas las tablas y guardarlas
        for j, table in enumerate(tables):
            # Guardar cada tabla en un archivo CSV con un nombre secuencial
            filename = f'tabla_{i+1}_parte_{j+1}.csv'
            table.to_csv(filename, index=False)
            print(f"Tabla {j+1} de '{url}' exportada con éxito como '{filename}'")

    except Exception as e:
        print(f"Error al procesar la URL '{url}': {e}")