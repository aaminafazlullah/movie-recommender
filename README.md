# 🎬 Movie Recommender App

A content-based movie recommender system built using Python, NLP, and Streamlit. It suggests movies based on similarity in metadata (genres, cast, keywords, etc.) and enriches recommendations with IMDb ratings, posters, and summaries using the OMDb API.

---

## 🚀 Features

- 🔎 Search any movie title
- 📊 Recommends similar movies using semantic similarity (TF-IDF + Cosine)
- 🧠 NLP-powered metadata cleaning
- 🖼️ Movie posters, ratings, and descriptions via OMDb API
- ➕ “Show More” button to dynamically load more suggestions
- 📱 Responsive UI built in Streamlit
- 🌐 Deployed using Streamlit Cloud

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **Backend**: Python
- **ML/NLP**: scikit-learn, NLTK, TF-IDF, cosine similarity
- **API**: OMDb API (for movie details)
- **Deployment**: Streamlit Cloud
- **Version Control**: Git + GitHub

---

## 📦 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/aaminafazlullah/movie-recommender.git
cd movie-recommender

# 2. (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate    # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up secrets
# Create a file at .streamlit/secrets.toml with your OMDb API key:
# OMDB_API_KEY = "your_actual_key"

# 5. Run the app
streamlit run app.py
