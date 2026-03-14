import pickle
from preprocessing import load_process
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = load_process()

vectorizer = TfidfVectorizer(stop_words='english')
matrix = vectorizer.fit_transform(df['tags'])
similarity = cosine_similarity(matrix)

pickle.dump(df, open("model/movies.pkl", "wb"))
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))
pickle.dump(similarity, open("model/similarity.pkl", "wb"))


