# Se importan librerias necesarias para el script
from fastapi import FastAPI, HTTPException
from functions import PlayTimeGenre, UserForGenre, recomendacion_usuario,UsersRecommend, sentiment_analysis, UsersWorstDeveloper
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import traceback  

templates = Jinja2Templates(directory="templates")

# Se genera una instancia de FastAPI
app = FastAPI()

@app.get("/")
async def root():
    """
    Recomendacion de videojuegos

    """
    return {"Mensaje": "Proyecto 1 Ricardo Santana"}


# 1
@app.get("/PlayTimeGenre/{genero}", tags=['PlayTimeGenre'])
async def endpoint1(genero: str):
    """
    Regresa año con más horas jugadas.
    
    Param:
        - genero (str): str
    """
    try:
        # Validación de valor nulo
        if not genero or not genero.strip():
            raise HTTPException(status_code=422, detail="El parámetro 'genero' no puede ser nulo o estar vacío.")

        result = PlayTimeGenre(genero)
    
        # Validación de existencia
        if not result:
            raise HTTPException(status_code=404, detail=f"No se encontró información para el género '{genero}'.")

        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo PlayTimeGenre.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")


# 2
@app.get("/UserForGenre/{genero}", tags=['UserForGenre'])
async def endpoint2(genero: str):
    """
    Retorna usuario con más horas jugadas por genero.

    Param:
        - genero (str): str

    """
    try:
        # Validación de valor nulo
        if not genero or not genero.strip():
            raise HTTPException(status_code=422, detail="El parámetro 'genero' no puede ser nulo o estar vacío.")

        result = UserForGenre(genero)
        
        # Validación de existencia
        if not result:
            raise HTTPException(status_code=404, detail=f"No se encontró información para el género '{genero}'.")
            
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo UserForGenre.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")


# 3
@app.get("/UsersRecommend/{year}", tags=['UsersRecommend'])
async def endpoint3(year: str):
    """
    Retorna top 3 juegos mas recomendados.
    
    Param:
        - year (str): int
    """
    try:
        year = int(year)
    
        if not (2000 <= year <= 2100):
            error_message = f"Valor entre 2000 y 2100 {str(e)}"
            return JSONResponse(status_code=500, content={"error": error_message})
        
        result = UsersRecommend(year)
    
        if result:
            return result
        else:
            error_message = "No hay recomendaciones"
            return JSONResponse(status_code=500, content={"error": error_message})

    except FileNotFoundError as e:
        error_message = f"Error en el archivo UsersRecommend.csv: {str(e)}"
        return JSONResponse(status_code=500, content={"error": error_message})

    except Exception as e:
        error_message = f"Error interno del servidor: {str(e)}"
        return JSONResponse(status_code=500, content={"error": error_message})


# 4
@app.get("/UsersWorstDeveloper/{year}", tags=['UsersWorstDeveloper'])
async def endpoint4(year: str):
    """
    Regresa top 3 desarrolladoras con juegos menos recomendados.
    
    Param:
        Year (str): int

    """
    try:
        year = int(year)
        result = UsersWorstDeveloper(year)
        return result
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error en el archivo UsersWorstDeveloper.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")


# 5
@app.get("/sentiment_analysis/{empresa_desarrolladora}", tags=['sentiment_analysis'])
async def enpoint5(empresa_desarrolladora: str):
    """
    Retorna diccionario con la cantidad total de reseñas.
    
    Param:
        empresa_desarrolladora (str): Str
    """
    try:
        result = sentiment_analysis(empresa_desarrolladora)
        return result
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error en el archivo sentiment_analysis.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")


# Item-item
@app.get("/recomendacion_usuario/{item_id}", tags=['recomendacion_usuario item_item'])
async def item(item_id: int):
    """
    Regresa listado con juegos recomendados similares al ingresado.
    
    Param:
        item_id (str): int
    """
    try:
        item_id = int(item_id) 
        resultado= recomendacion_usuario(item_id)
        return resultado
    except Exception as e:
        return {"error":str(e)}