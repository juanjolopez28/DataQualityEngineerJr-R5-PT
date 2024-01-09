# DataQualityEngineerJr-R5-PT

## 1. INTRODUCCION
Se ha demostrado que los datos son la clave para entregar valor a los clientes y estos son una parte integral de tu estrategia comercial. Además, son un activo importante de todas las empresas. 

El presente  reporte de calidad de datos - Spotify API forma parte del  proceso de selección para el cargo de Data Quality Engineer Junior en la empresa R5.

Esta propuesta busca explicar a detalle el proceso de indentificación de todas las anomalías de calidad de datos del dataset obtenido de la API de Spotify (dataset entregado como parte de la prueba), cabe resaltar que el reporte se basa en las seis dimensiones principales para la evaluación de la calidad de los datos 

---
## 2. CONSIDERACIONES
- El archivo : [Clean data](./clean_data.py) , hace referencia a la primera parte del proceso donde se exportan los datos del [Dataset](./DB/taylor_swift_spotify.json) a archivo .csv , como propuesta se obtuvieron dos archivos csv:
  - [Dataset_Albums](./DB/dataset_albumes.csv): Archivo con los datos de albums desanidados.
  - [Dataset](./DB/dataset.csv): Archivo completo con el campo "albums" y "tracks" desanidados.
- El archivo: [Data Quality Analysis](./data_quality_analysis.ipynb) , hace referencia a la segunda parte del proceso, donde se detalla paso a paso la identificación de anomalías del dataset, mediante el lenguaje de programación python.
- El archivo [Reporte](./Reporte.pdf) , hace referencia al reporte respectivo de la prueba.
