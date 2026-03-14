import pandas as pd
import ast
def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

def convert3(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter+=1
        else:
            break
    return L

def fetchdirector(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L

def load_process():
    movies = pd.read_csv("data/tmdb_5000_movies.csv")
    credits = pd.read_csv("data/tmdb_5000_credits.csv")
    movies = movies.merge(credits,on="title")
    movies = movies[['title','overview','genres','keywords','cast','crew']]
    movies.dropna(inplace=True)
    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    movies['cast'] = movies['cast'].apply(convert3)
    movies['crew'] = movies['crew'].apply(fetchdirector)

    movies['overview'] = movies['overview'].apply(lambda x: x.split())

    movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
    movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
    movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
    movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])

    movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
    movies['tags'] = movies['tags'].apply(lambda x:" ".join(x))

    new_df = movies[['title','tags']]
    return new_df