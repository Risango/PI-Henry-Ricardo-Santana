# Proyecto Individual: Sistema de Recomendación de Videojuegos

## Descripción del Proyecto
Este proyecto desarrolla un sistema de recomendación de videojuegos utilizando técnicas de machine learning y operaciones de MLOps. Como Data Scientist en una plataforma multinacional de videojuegos, el objetivo es crear un modelo que recomiende videojuegos a los usuarios basándose en su historial y preferencias.

## Estructura del Repositorio
- `functions.py`: Contiene las funciones utilizadas para generar recomendaciones y análisis de datos.
- `main.py`: API de FastAPI que sirve los resultados del modelo a los usuarios.
- Notebooks de Jupyter:
  - `EDA.ipynb`: Análisis exploratorio de los datos (EDA) para entender las características de los datos.
  - `itemItem.ipynb`: Notebook para el modelado de recomendaciones basado en el filtrado colaborativo.
  - `userReviews.ipynb`, `userItems_ETL.ipynb`, `steamGames_ETL.ipynb`, `transform.ipynb`: Notebooks que realizan la extracción, transformación y carga (ETL) de los datos utilizados en el modelo.

## Funcionalidades Implementadas
### API Endpoints:
- **`/`**: Endpoint principal que muestra un mensaje de bienvenida.
- **`/PlayTimeGenre/{genero}`**: Devuelve el año con más horas jugadas por género.
- **`/UserForGenre/{genero}`**: Devuelve el usuario que más horas ha jugado en un género específico.
- **`/UsersRecommend/{year}`**: Retorna una lista de recomendaciones de usuarios para un año dado.
- **`/UsersWorstDeveloper/{year}`**: Muestra los desarrolladores con peor desempeño o críticas en un año específico.
- **`/SentimentAnalysis/{developer}`**: Realiza un análisis de sentimiento sobre los comentarios relacionados con un desarrollador específico.
- **`/RecommendationUser/{item_id}`**: Recomienda videojuegos similares basados en un ID de videojuego específico.

### Análisis de Datos:
- **Exploración de Datos (EDA)**: Utilizado para identificar tendencias y patrones en los datos de videojuegos y reseñas de usuarios.
- **Visualizaciones**: Creación de gráficos y nubes de palabras para representar visualmente la data y extraer insights.

### Modelo de Recomendación:
- **Filtrado Colaborativo**: Implementación de un sistema de recomendación que sugiere videojuegos a los usuarios basándose en algoritmos de filtrado colaborativo.

### Procesos ETL:
- **Transformación y Limpieza de Datos**: Notebooks como `userItems_ETL.ipynb` y `steamGames_ETL.ipynb` manejan la extracción, transformación y carga de los datos, preparándolos para el análisis y la modelación.
- **Automatización**: Implementación de scripts para automatizar la recolección y procesamiento de datos, facilitando actualizaciones y mantenimientos continuos.

## Tecnologías Utilizadas
- Python
- FastAPI
- Pandas, Matplotlib
- Jupyter

## Autores
- Ricardo Santana
