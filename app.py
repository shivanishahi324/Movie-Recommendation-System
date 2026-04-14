import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import os

# -------------------------------
# Load similarity from Google Drive 
# -------------------------------
@st.cache_resource
def load_similarity():
    file_id = "1VLglft-aUiGAHYbPWH8HfQt2hdlXyH6Z"
    output = "similarity.pkl"

    if not os.path.exists(output):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output, quiet=False)

    return pickle.load(open(output, "rb"))


# -------------------------------
# Fetch movie poster
# -------------------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=3841e9ba7e48000ca352e94021c913ea&language=en-US"
    data = requests.get(url).json()

    poster_path = data.get('poster_path')

    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return "https://via.placeholder.com/500x750"


# -------------------------------
# Recommendation logic
# -------------------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))

    return names, posters


# -------------------------------
# Load data
# -------------------------------
@st.cache_data
def load_movies():
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    return pd.DataFrame(movies_dict)

movies = load_movies()
similarity = load_similarity()


# -------------------------------
# UI
# -------------------------------
st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values
)

if st.button('Recommend'):
    with st.spinner("Fetching recommendations..."):
        names, posters = recommend(selected_movie_name)

    st.subheader("Top 5 Recommendations")

    cols = st.columns(5)

    for i in range(len(names)):
        with cols[i]:
            st.caption(names[i])
            st.image(posters[i])
