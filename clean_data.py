import pandas as pd
from pandas import json_normalize

import os

def json_to_csv():
    #Verificamos encontrar la ruta respectiva en cualquier entorno
    ruta_script = os.path.abspath(__file__)
    directorio_actual = os.path.dirname(ruta_script)
    ruta_json = os.path.join(directorio_actual, 'DB', 'taylor_swift_spotify.json')

    with open(ruta_json, 'r') as json_file:
        data = pd.read_json(json_file)

    # Descompemos la columna 'albums' por ser anidada
    data_descompuesto_albums = pd.concat([data.drop(['albums'], axis=1), json_normalize(data['albums'])], axis=1)

    # Descomponemos la columna 'tracks' utilizando explode
    df = data_descompuesto_albums.explode('tracks').reset_index(drop=True)

    # Descomponemos las columnas anidadas dentro de 'tracks'
    df_final = pd.json_normalize(df['tracks'], sep='_')

    # Combinamos los DataFrames
    df_resultado = pd.concat([df.drop(['tracks'], axis=1), df_final], axis=1)

    #Exportamos a un archivo csv
    df_resultado.to_csv('DB/dataset.csv', index=False)
    

if __name__ == "__main__":
    json_to_csv()
