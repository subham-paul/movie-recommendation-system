# 🎬 Movie Recommendation System

A smart **Movie Recommendation System** built with **Python** and **Flask** that helps users discover movies based on their interests and preferences. Using **Machine Learning** and **Content-Based Filtering**, the application recommends similar movies by analyzing genres, cast, crew, keywords, and other movie metadata.

> **Discover your next favorite movie with the power of Artificial Intelligence.**

---

# ✨ Features

- 🎥 Personalized movie recommendations
- 🤖 AI-powered recommendation engine
- 🔍 Search movies by title
- 🎬 Similar movie suggestions
- 📊 Content-Based Filtering
- ⚡ Fast recommendation generation
- 🌐 Responsive Flask web interface
- 🖼️ Movie poster integration *(if TMDB API is used)*
- 📖 Movie overview and details

---

# 🛠️ Tech Stack

## Backend

- Python 3.x
- Flask

## Machine Learning

- Scikit-learn
- Pandas
- NumPy

## Recommendation Engine

- Content-Based Filtering
- Cosine Similarity
- NLP (Feature Extraction)

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Jinja2 Templates

---

# 📂 Project Structure

```text
movie-recommendation-system/
│
├── app.py
├── requirements.txt
├── model/
│   ├── movies.pkl
│   ├── similarity.pkl
│   └── ...
│
├── dataset/
│   ├── movies.csv
│   └── credits.csv
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── recommendation.html
│   └── ...
│
├── README.md
│
└── ...
```

---

# 🚀 Features Overview

- 🎬 Movie Search
- 🤖 AI Recommendation Engine
- 📊 Similar Movie Suggestions
- 🎥 Movie Poster Display
- ⭐ Movie Details
- ⚡ Fast Prediction
- 🌐 Web-Based Interface
- 📱 Responsive Design
- 💾 Pre-trained Recommendation Model
- 🔍 Intelligent Search

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/subham-paul/movie-recommendation-system.git
```

```bash
cd movie-recommendation-system
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables *(Optional)*

If using the TMDB API for movie posters and details, create a `.env` file:

```env
TMDB_API_KEY=your_api_key_here
SECRET_KEY=your_secret_key
```

---

## 5. Run the Application

```bash
python app.py
```

or

```bash
flask run
```

---

# 🌐 Open in Browser

```
http://127.0.0.1:5000
```

---

# 📝 How It Works

1. Search for a movie by its title.
2. The application locates the selected movie in the dataset.
3. A content-based filtering algorithm calculates similarities between movies.
4. Cosine similarity identifies the closest matches.
5. The system displays a list of recommended movies along with additional details such as posters and descriptions (if available).

---

# 📊 Recommendation Technique

The recommendation engine uses **Content-Based Filtering**, which compares movies based on features such as:

- 🎭 Genres
- 🎬 Cast
- 🎥 Director
- 📝 Keywords
- 📖 Overview
- ⭐ Movie Metadata

Cosine Similarity is then used to measure how closely related two movies are and generate personalized recommendations.

---

# 📊 Applications

- Movie Streaming Platforms
- Entertainment Portals
- OTT Recommendation Systems
- AI Recommendation Projects
- Educational Machine Learning Projects
- Personalized Content Discovery

---

# 🚀 Future Enhancements

- 🤖 Collaborative Filtering
- 🧠 Hybrid Recommendation System
- 🎭 Genre-Based Filtering
- ⭐ User Ratings & Reviews
- 👤 User Authentication
- ❤️ Favorite Movies
- 📈 Trending Movies
- 🌍 Multi-language Support
- ☁️ Cloud Deployment
- 📱 Mobile-Friendly UI

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.

2. Create a feature branch.

```bash
git checkout -b feature/NewFeature
```

3. Commit your changes.

```bash
git commit -m "Add New Feature"
```

4. Push your changes.

```bash
git push origin feature/NewFeature
```

5. Open a Pull Request.

---

# 🐞 Reporting Issues

If you find any bugs or have suggestions for improvements, please open an issue with detailed information.

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## **Subham Paul**

Passionate about **Python, Artificial Intelligence, Machine Learning, Data Science, Flask, and Web Development.**

- GitHub: https://github.com/subham-paul
- LinkedIn: https://www.linkedin.com/in/subham-paul-india/

---

# ⭐ Show Your Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork the project
- 🤝 Contribute
- 💬 Share your feedback


---

## 🙏 Acknowledgements

Special thanks to the open-source communities behind:

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- TMDB API *(if used)*
- Bootstrap

for providing the technologies that made this project possible.

---

> **"Helping you discover great movies—one recommendation at a time."** 🎬🍿
