#User Items
#Importo Librerias
import pandas as pd


#Funcion PlayTimeGenre
def PlayTimeGenre(genre):
    
    # Creo Dataframe a partir de Arcghivo csv
    df_playtimegenre= pd.read_csv('./Dataset/df_PlayTimeGenre.csv')
    
    #Filtro Dataframe por genero
    df_filtered_by_genre = df_playtimegenre[df_playtimegenre['genres'] == genre]
    
    #Calculo numero de horas por genero y año
    gender_hours = df_filtered_by_genre.groupby('release_date')['playtime_forever'].sum()
    
    #Calculo el año con numero maximo de horas 
    max_time_play_gender = gender_hours.idxmax()
    
    #Creo diccioanrio Año de lanzamiento con más horas jugadas para el Género 
    result = {
    "Año de lanzamiento con más horas jugadas para Género {}".format(genre) : max_time_play_gender
    }
    return result


#Funcion UserForGenre
def UserForGenre(genre):
    
    # Creo Dataframe a partir de Arcghivo csv
    # df_userforgenre= pd.read_csv('/content/drive/MyDrive/PI_ML_OPS-PT/Dataset/df_UserForGenre.csv')
    df_userforgenre= pd.read_csv('./Dataset/df_UserForGenre.csv')
    
    #Filtro Dataframe por genero
    df_filtered_by_genre = df_userforgenre[df_userforgenre['genres']==genre]
    
    #Calculo numero de horas por usuario y año
    user_hours = df_filtered_by_genre.groupby('user_id')['playtime_forever'].sum()
    
    #Calculo el usuario con numero maximo de horas 
    max_time_play_user = user_hours.idxmax()
    
    #Filtro por el usuario con mas horas
    max_user_df = df_filtered_by_genre[df_filtered_by_genre['user_id'] == max_time_play_user]
    
    #Filtro usuario por año y horas
    hours_by_year = max_user_df.groupby('release_date')['playtime_forever'].sum().reset_index()
    
    #Creo lista de año y horas jugadas del usuario
    hours_years_list = [
        {'Año':year, 'Horas': hours} for year, hours in zip(hours_by_year['release_date'],hours_by_year['playtime_forever'])
                        ]
    #Creo Diccionario del genero y usuario con mas horas por cada año
    result = {
    'Usuario con más horas jugadas para genero {}'.format(genre):max_time_play_user,
    'Horas jugadas': hours_years_list
    }
    return result

#Funcion UsersRecommend
def UsersRecommend(year):

    # Creo Dataframe a partir de Arcghivo csv   
    # df_userforgenre= pd.read_csv('/content/drive/MyDrive/PI_ML_OPS-PT/Dataset/df_UserForGenre.csv')
    df_usersrecommend= pd.read_csv('./Dataset/df_UsersRecommend.csv')

    #Filtro usuarios recomendados por año
    df_filtered_by_year = df_usersrecommend[df_usersrecommend['release_date']==year]

    #Filtro los 3 juegos mas recomendados del año
    top_games = df_filtered_by_year['app_name'].value_counts().head(3)

    #Convertir el resultado a un formato de lista de diccionarios
    result = [{"Puesto numero {} más recomendado es".format(i+1): juego} for i, juego in enumerate(top_games.index)]
    return result

#Funcion UsersRecommend
def UsersNotRecommend(year):
    
    # Creo Dataframe a partir de Arcghivo csv
    # df_userforgenre= pd.read_csv('/content/drive/MyDrive/PI_ML_OPS-PT/Dataset/df_UserForGenre.csv')
    df_usersnotrecommend= pd.read_csv('./Dataset/df_UsersNotRecommend.csv')

    #Filtro los 3 juegos menos recomendados del año
    df_filtered_by_year = df_usersnotrecommend[df_usersnotrecommend['release_date']==year]

    #Filtro los 3 juegos menos recomendados del año
    top_games = df_filtered_by_year['app_name'].value_counts().head(3)

    #Convertir el resultado a un formato de lista de diccionarios
    result = [{"Puesto numero {} menos recomendado es".format(i+1): juego} for i, juego in enumerate(top_games.index)]
    return result

#Funcion sentiment_analysis
def sentiment_analysis(year):

    # df_sentiment_analysis= pd.read_csv('/content/drive/MyDrive/PI_ML_OPS-PT/Dataset/df_sentiment_analysis.csv')
    df_sentiment_analysis= pd.read_csv('./Dataset/df_sentiment_analysis.csv')

    # Filtra por año
    df_filtered_by_year = df_sentiment_analysis[df_sentiment_analysis['release_date']==year]

    # Ordena por release_date y sentiment_analysis
    df_filtered_by_year = df_filtered_by_year.sort_values(by=['release_date', 'sentiment_analysis'])

    # Resetea el indice
    df_filtered_by_year.reset_index(drop=True, inplace=True)

    # Agrupa por nombre y suma Counted
    sentiment_counts = df_filtered_by_year.groupby('nombre')['Counted'].sum()

    # Muestra los conteos en formato diccionario
    result_dict = sentiment_counts.to_dict()
    return result_dict