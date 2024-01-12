from funciones import *
from fastapi import FastAPI
import pandas as pd
app = FastAPI()
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000, debug=True)


# Ruta de bienvenida
@app.get('/')
def bienvenida():
    """
    Hola, bienvenido a mi API, mi nombre es Manuel Carruitero,
    actualmente estoy elaborando un proyecto para mi cursada en Henry
    y este es el resultado.
    Un gusto que estes aqui, que lo disfrutes.
    """
    return {'API de consultas a una base de datos de Steam, /docs en el link para acceder a las funciones de consulta.'}

# Ruta para la función PlayTimeGenre
@app.get('/play_time_genre/{genre}')
def play_time_genre(genre: str):
    """
    Esta funcion calcula el año con mas horas jugadas para un genero dado por el usuario.
    genero:str Genero
    """
    result = PlayTimeGenre(genre)
    return {'result': result}

# Ruta para la función UserForGenre
@app.get('/user_for_genre/{genre}')
def user_for_genre(genre: str):
    """
    Esta funcion calcula para un Genero el usuario con mas horas acumuladas devuelve el id del usuario y las horas acumuladas
    params:
    genero:str Genero
    """
    result = UserForGenre(genre)  
    return {'result': result}

# Ruta para la función UsersRecommend
@app.get('/users_recommend/{year}')
def users_recommend(year: int):
    """
    Esta funcion para un año dado por el usuario, los 3 juegos mas recomendados.
    params:
    año:int Año
    """
    result = UsersRecommend(year)
    return {'result': result}

# Ruta para la función UsersNotRecommend
@app.get('/users_not_recommend/{year}')
def users_not_recommend(year: int):
    """
    Esta funcion para un año dado por el usuario, los 3 juegos menos recomendados.
    params:
    año:int Año
    """
    result = UsersNotRecommend(year)
    return {'result': result}

# Ruta para la función sentiment_analysis
@app.get('/sentiment_analysis/{year}')
def sentiment_analysis(year: int):
    """
    Esta funsion para un año dado por el usuario, la cantidad de calificaciones malas buenas y neutrales.
    params:
    año:int Año
    """
    try:
        result = sentiment_analysis(year)
        return {'result': result}
    except Exception as e:
        return {'error': f"Error al procesar la solicitud: {str(e)}"}