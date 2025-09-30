a) Descripción del dataset

El dataset Netflix Titles contiene información sobre las películas y programas de televisión disponibles en la plataforma. Incluye datos como título, director, país, tipo de contenido (Movie o TV Show), año de lanzamiento, fecha de incorporación a Netflix, duración, géneros y una breve descripción.

b) Información del resumen estadístico

El resumen estadístico obtenido con describe() muestra principalmente datos de las columnas numéricas, como:

Cantidad de registros válidos (count).

Promedio de los valores (mean).

Desviación estándar (std), que mide la dispersión de los datos.

Mínimo y máximo (min y max).

Percentiles (25%, 50%, 75%), que ayudan a conocer cómo se distribuyen los valores.

Si se usara include='all', también mostraría información sobre columnas categóricas, como el número de categorías y la frecuencia de la más común.

c) Cambios o tendencias detectadas

Aumenta la cantidad de títulos recientes, sobre todo después del año 2015.

Existen registros de producciones muy antiguas (décadas de 1920–1940), pero son pocos casos.

Se observa una expansión progresiva del catálogo, concentrándose en los últimos 10 a 15 años.

d) Categorías que sobresalen

Tipo de contenido: predominan las películas frente a las series, ya que históricamente Netflix ofrecía más de este tipo de contenido.

Año de lanzamiento: destacan las producciones del siglo XXI, debido al crecimiento de la industria digital.

Géneros: aunque no se analizaron directamente en el código, el dataset muestra que Drama y Comedia son de los más frecuentes, lo que coincide con la alta demanda de estos géneros.

e) Diferencias entre primeros y últimos registros

Los primeros registros (head()) muestran títulos iniciales en el orden del archivo, que incluyen producciones más antiguas.

Los últimos registros (tail()) reflejan títulos más recientes y permiten observar cómo ha evolucionado el catálogo.
Esto evidencia el cambio en la oferta de contenidos a lo largo del tiempo.

f) Aportes de las medidas estadísticas

Al calcular la media, mediana y desviación estándar sobre la columna release_year:

Media (~2013): la mayor parte de los títulos son de los últimos 10–15 años.

Mediana (2017): la mitad de los títulos se concentran en el 2017 en adelante.

Desviación estándar (~8 años): refleja que la mayoría de lanzamientos están cerca en el tiempo, aunque existen valores atípicos (títulos muy antiguos).

#Integrantes;  ELIAS ERNESTO ORELLANA VAZQUES SMSS211023
               ARIEL ADOLFO DIAZ SOSA   SMSS109224
