import pickle
import re

from rapidfuzz import process
from rapidfuzz import fuzz

df = pickle.load(open("model/movies.pkl","rb"))
similarity = pickle.load(open("model/similarity.pkl","rb"))

def normalize(title):
    title = title.lower()
    title = re.sub(r'[^a-z0-9]', '', title)
    return title

def recommend(movie):
    idx = df[df['title'] == movie].index[0]
    distances = list(enumerate(similarity[idx]))
    distances = sorted(distances,key=lambda x: x[1], reverse=True)
    recommendations = []
    for i in distances[1:6]:
        recommendations.append(df.iloc[i[0]].title)
    return recommendations

movie = input("Enter a movie name: ")
titles = df['title'].tolist()

normalized_titles = [normalize(t) for t in titles]
normalized_movie = normalize(movie)

match = process.extractOne(normalized_movie,normalized_titles,scorer=fuzz.token_sort_ratio)

matched = titles[match[2]]

if match[1] < 60:
    print("Movie not found.")
    exit()

print("Closest match: ",matched)
results = recommend(matched)
print("Recommended movies: ")
for r in results:
    print(r)