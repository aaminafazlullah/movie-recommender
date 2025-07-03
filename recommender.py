import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import nltk
import os
api_key = os.getenv("api_key")
import requests
def get_movie_details(movie_title):
  response = requests.get(f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}")
  data = response.json()
  if data.get('Response') == 'True':
    return {
        "title": data.get("Title"),
        "imdb_id": data.get("imdbID"),
        "rating": data.get("imdbRating"),
        "poster": data.get("Poster"),
        "plot": data.get("Plot")
    }
  else:
    return None
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
movies_data = pd.read_csv('movies.csv')
def clean_text(text):
  if not isinstance(text, str):
    return ""
  text = re.sub('[^a-zA-Z]', ' ', text)
  text = text.lower()
  words = text.split()
  words = [stemmer.stem(w) for w in words if w not in stop_words]
  return ' '.join(words)
movies_data['processed_overview'] = movies_data['overview'].apply(clean_text)
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director', 'processed_overview']
for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')
combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director'] + ' ' + movies_data['processed_overview']
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
similarity = cosine_similarity(feature_vectors)
list_of_all_titles = [title.lower() for title in movies_data['title'].tolist()]
def recommend(title, count = 5):
  title = title.lower()
  if title not in list_of_all_titles:
    return "Movie not found."
  find_close_match = difflib.get_close_matches(title, list_of_all_titles)
  close_match = find_close_match[0]
  index_of_the_movie = movies_data[movies_data['title'].str.lower() == close_match]['index'].values[0]
  similarity_score = list(enumerate(similarity[index_of_the_movie]))
  recommended_movies = sorted(similarity_score, key = lambda x: x[1], reverse = True)[1:count + 1]
  recommended_titles = [movies_data.iloc[i[0]]['title'] for i in recommended_movies]
  return recommended_titles