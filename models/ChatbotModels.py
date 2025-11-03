import os
import pandas as pd
import joblib

# --- Load data & model ---
# Dapatkan path absolut folder proyek utama (naik dua level dari file ini)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Sekarang BASE_DIR = .../chatbot-API
# Maka naik satu lagi ke folder chatbot
PROJECT_ROOT = os.path.join(BASE_DIR, "..", "chatbot")

# Path file relatif dari folder chatbot
DATA_PATH = os.path.join(PROJECT_ROOT, "preprocessing", "data_all_clean.csv")
TFIDF_VECTORIZER_PATH = os.path.join(PROJECT_ROOT, "tfidf_data", "tfidf_vectorizer.pkl")
TFIDF_MATRIX_PATH = os.path.join(PROJECT_ROOT, "tfidf_data", "tfidf_matrix.pkl")
EMBED_MODEL_PATH = os.path.join(PROJECT_ROOT, "embedding_data", "sentence_embedding_model.pkl")
EMBEDDINGS_PATH = os.path.join(PROJECT_ROOT, "embedding_data", "sentence_embeddings.pkl")

print("📁 Current working directory:", os.getcwd())
print("📄 File path to load:", DATA_PATH)
print("📄 File exists?", os.path.exists(DATA_PATH))

df_all = pd.read_csv(DATA_PATH)
vectorizer = joblib.load(TFIDF_VECTORIZER_PATH)
tfidf_matrix = joblib.load(TFIDF_MATRIX_PATH)
model = joblib.load(EMBED_MODEL_PATH)
embeddings = joblib.load(EMBEDDINGS_PATH)
