import pandas as pd
import os
import json

def json_to_csv():
    #Verificamos encontrar la ruta respectiva en cualquier entorno
    ruta_script = os.path.abspath(__file__)
    directorio_actual = os.path.dirname(ruta_script)
    ruta_json = os.path.join(directorio_actual, 'DB', 'taylor_swift_spotify.json')

    with open(ruta_json, 'r') as json_file:
        data = pd.read_json(json_file)
    data.to_csv('DB/archivo.csv', index=False)

if __name__ == "__main__":
    json_to_csv()
