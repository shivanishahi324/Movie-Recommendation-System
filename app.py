import streamlit as st
import pickle
import pandas as pd
import requests

# Load similarity from Google Drive
import gdown
import os

def load_similarity():
    file_id = "1VLglft-aUiGAHYbPWH8HfQt2hdlXyH6Z"
    output = "similarity.pkl"

    if not os.path.exists(output):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output, quiet=False)

    return pickle.load(open(output, "rb"))

# Fetch movie poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=3841e9ba7e48000ca352e94021c913ea&language=en-US"
    data = requests.get(url).json()

    poster_path = data.get('poster_path')

    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750"

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# Load movie data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Load similarity matrix from Drive
similarity = load_similarity()

# UI
st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
