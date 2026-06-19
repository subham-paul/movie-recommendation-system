# ================================
# Movie Recommendation System
# Backend: Flask (Production Ready)
# ================================

import os
import pandas as pd
import numpy as np

from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

# -------------------------------
# App Configuration
# -------------------------------
load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "cinemind-ai-secret")

# -------------------------------
# Load & Validate Dataset
# -------------------------------
DATA_PATH = "data/movies.csv"

def load_movies(path):
    if not os.path.exists(path):
        raise FileNotFoundError("❌ data/movies.csv not found")

    if os.stat(path).st_size == 0:
        raise ValueError("❌ movies.csv is empty")

    df = pd.read_csv(path)

    required_columns = {
        "id", "title", "genre", "overview",
        "popularity", "vote_average", "vote_count"
    }

    if not required_columns.issubset(df.columns):
        raise ValueError(
            f"❌ Dataset must contain columns: {required_columns}"
        )

    # Clean data
    df["overview"] = df["overview"].fillna("")
    df["genre"] = df["genre"].fillna("")
    df["title"] = df["title"].fillna("Unknown Title")

    # Remove duplicates
    df = df.drop_duplicates(subset="title")

    return df.reset_index(drop=True)

movies_df = load_movies(DATA_PATH)

# -------------------------------
# Feature Engineering
# -------------------------------
movies_df["combined_features"] = (
    movies_df["overview"] + " " + movies_df["genre"]
)

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=8000,
    ngram_range=(1, 2)
)

tfidf_matrix = vectorizer.fit_transform(
    movies_df["combined_features"]
)

cosine_sim = cosine_similarity(tfidf_matrix)

# Mapping titles to index
indices = pd.Series(
    movies_df.index,
    index=movies_df["title"].str.lower()
).drop_duplicates()

# -------------------------------
# Recommendation Engine
# -------------------------------
def recommend_movies(title, top_n=10):
    title = title.lower()

    if title not in indices:
        return []

    idx = indices[title]

    similarity_scores = list(enumerate(cosine_sim[idx]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )[1:top_n + 1]

    movie_indices = [i[0] for i in similarity_scores]

    results = movies_df.iloc[movie_indices]

    # Sort by popularity & rating (hybrid ranking)
    results = results.sort_values(
        by=["vote_average", "popularity"],
        ascending=False
    )

    return results[[
        "title",
        "genre",
        "overview",
        "vote_average",
        "popularity",
        "release_date"
    ]].to_dict(orient="records")

# -------------------------------
# Routes
# -------------------------------
@app.route("/")
def index():
    trending = movies_df.sort_values(
        by="popularity",
        ascending=False
    ).head(8)

    return render_template(
        "index.html",
        trending=trending.to_dict(orient="records")
    )

@app.route("/dashboard")
def dashboard():
    movie_list = sorted(movies_df["title"].unique().tolist())
    return render_template("dashboard.html", movies=movie_list)

@app.route("/recommend", methods=["POST"])
def recommend():
    movie_name = request.form.get("movie")

    if not movie_name:
        return jsonify({"error": "Movie name is required"}), 400

    recommendations = recommend_movies(movie_name)

    if not recommendations:
        return jsonify({"error": "Movie not found in database"}), 404

    return jsonify(recommendations)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# -------------------------------
# Run Application
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
