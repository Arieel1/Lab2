import pandas as pd
import numpy as np

# 1. Cargar el dataset CSV de Netflix 
DatosNetflix = pd.read_csv("netflix_titles.csv")

# 2. Verificar carga correcta del dataset y mostrar estructura básica del DataFrame (aunque en este parte me pierdo)
print("Dataset cargado correctamente")
print("Número de Filas y Columnas:", DatosNetflix.shape)
print("\nPrimeras Filas del Dataset:")
print(DatosNetflix.head())

# 3. Resumen estadístico con describe() 
print("\nResumen Estadístico del Dataset:")
print(DatosNetflix.describe())

# 4. Tipos de datos de cada columna 
print("\nTipos de Datos de Cada Columna:")
print(DatosNetflix.dtypes)

print("\nAnálisis posible según tipo de dato:")
print("- Columnas numéricas (int/float): permiten medias, medianas, desviaciones, ordenamientos.")
print("- Columnas de texto (object): permiten conteos, filtrados, categorías.")
print("- Fechas (object/datetime): permiten análisis temporal y tendencias.")

# 5. Mostrar primeros y últimos registros 
print("\n Primeros Registros:")
print(DatosNetflix.head())

print("\n Últimos Registros:")
print(DatosNetflix.tail())

# 6. Ordenar resultados para ver categorías destacadas 
#Dato que nose si sea relevante pero al poner el release_year me da menos problemas que al colocarlo ene español, nose si es por el encoding o que 
#lo menciono porque en el dataset original viene en español pero al abrirlo con pandas me lo traduce automáticamente al inglés y me da error
print("\nTítulos ordenados por Año de Lanzamiento (más recientes primero):")
print(DatosNetflix.sort_values(by="release_year", ascending=False).head(10))

print("\nTítulos ordenados por Año de Lanzamiento (más antiguos primero):")
print(DatosNetflix.sort_values(by="release_year", ascending=True).head(10))

# 7. Medidas estadísticas sobre una columna numérica
# Usaremos la columna "release_year" para calcular media, mediana y desviación estándar 
# Pero para ser sincero no sé si es la más adecuada, ya que es un año y no una medida continua de cantidad o tamaño pero es lo que tenemos xd
Anios = DatosNetflix["release_year"]

Media = np.mean(Anios)
Mediana = np.median(Anios)
Desviacion = np.std(Anios)

print("\nMedidas Estadísticas de 'release_year':")
print(f"Media: {Media}")
print(f"Mediana: {Mediana}")
print(f"Desviación Estándar: {Desviacion}")
