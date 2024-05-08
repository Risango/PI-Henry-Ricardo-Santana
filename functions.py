# Se importan librerías necesarias
import pandas as pd

def PlayTimeGenre(genero: str):
    result_df = pd.read_csv('PlayTimeGenre.csv')
    filtered_df = result_df[result_df['genres'] == genero]
    grouped_df = filtered_df.groupby('year')['hours_game'].sum()
    max_hours_year = grouped_df.idxmax()
    response_data = {"Año con más horas jugadas para {}: {}".format(genero, max_hours_year)}
    return response_data


def UserForGenre(genero:str):
    consulta2 = pd.read_csv('UserForGenre.csv')
    genre_data = consulta2[consulta2['genres'] == genero]
    top_user = genre_data.loc[genre_data['hours_game'].idxmax()]['user_id']
    hours_by_year = genre_data.groupby('year')['hours_game'].sum().reset_index()
    hours_by_year = hours_by_year.rename(columns={'year': 'Año', 'hours_game': 'Horas'})
    hours_list = hours_by_year.to_dict(orient='records')
    result = {
        "Usuario con más horas jugadas": top_user,
        "Horas jugadas": hours_list
    }
    return result


def UsersRecommend(year: int):
    df = pd.read_csv('UsersRecommend.csv')
    result_df = df[df['year'] == year]
    response_data = [{"1ro": result_df.iloc[0]['name']},
                     {"2do": result_df.iloc[1]['name']},
                     {"3ro": result_df.iloc[2]['name']}]
    return response_data


def UsersWorstDeveloper(year: int):
    df = pd.read_csv('UsersWorstDeveloper.csv')
    result_df = df[df['year'] == year]
    ret = [{"1ro": result_df.iloc[0]['developer']},
                    {"2do": result_df.iloc[1]['developer']},
                    {"3ro": result_df.iloc[2]['developer']}]
    return ret

def sentiment_analysis(empresa_desarrolladora: str):
    df = pd.read_csv('sentiment_analysis.csv')
    result_df = df[df['developer'] == empresa_desarrolladora]
    response_data = result_df.set_index('developer').to_dict(orient='index')
    return response_data


def recomendacion_usuario(item_id):
    df = pd.read_csv('recomienda_item_item.csv')
    result_df = df[df['item_id'] == item_id]
    response_data = result_df['Recomendaciones']
    return response_data

