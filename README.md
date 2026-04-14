# Movie Recommendation System

A production-ready machine learning project demonstrating content-based recommendation systems, API integration, and cloud deployment using Streamlit.

---

## Live Demo

https://movie-recommendation-system-szzfbmzwtxscxyccj7enzd.streamlit.app/

---

## Features

* Content-based filtering using cosine similarity
* Generates top 5 similar movie recommendations
* Interactive web interface built with Streamlit
* Real-time movie poster fetching using TMDB API
* Efficient handling of large similarity matrix via Google Drive

---

## How It Works

* Movie metadata is preprocessed and converted into feature vectors
* Cosine similarity is computed between all movies
* Based on the selected movie, the top 5 most similar movies are retrieved
* Posters are dynamically fetched using the TMDB API

---

## Tech Stack

* Python
* Pandas, NumPy, Scikit-learn
* Streamlit
* TMDB API
* Google Drive (external storage for large model files)

---

## Project Structure

```
├── app.py
├── movie_dict.pkl
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### Clone the repository

```
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run the application

```
streamlit run app.py
```

---

## Notes

* The similarity matrix file is large and stored externally on Google Drive
* It is automatically downloaded at runtime

---

## Future Improvements

* Add genre-based filtering
* Improve recommendation accuracy using advanced NLP techniques
* Extend to collaborative filtering
* Enhance UI/UX

---

## Author

Shivani Shahi
B.Tech Electrical Engineering
Machine Learning & Data Science Enthusiast

---

## Acknowledgment

Movie data and posters are provided by The Movie Database (TMDB) API.
