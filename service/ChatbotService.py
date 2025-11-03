from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity    
from textwrap import dedent
import joblib, pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os


from models.ChatbotModels import df_all, vectorizer, tfidf_matrix, embeddings, model

# --- LLM Membuatkan teksnya ---
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)
model_llm = genai.GenerativeModel("gemini-2.5-flash")

def get_chatbot_response(query: str) :
    # --- Hitung similarity ---
    query_tfidf = vectorizer.transform([query])
    sim_tfidf = cosine_similarity(query_tfidf, tfidf_matrix)[0]

    query_embed = model.encode([query])
    sim_embed = cosine_similarity(query_embed, embeddings)[0]

    # --- Normalisasi ---
    scaler = MinMaxScaler() 
    sim_tfidf_norm = scaler.fit_transform(sim_tfidf.reshape(-1, 1)).flatten()
    sim_embed_norm = scaler.fit_transform(sim_embed.reshape(-1, 1)).flatten()

    # --- Gabung skor (weighted fusion) ---
    w_tfidf, w_embed = 0.4, 0.6
    hybrid_score = (w_tfidf * sim_tfidf_norm) + (w_embed * sim_embed_norm)

    # --- Ambil top-N context ---
    N = 3
    top_indices = np.argsort(hybrid_score)[-N:][::-1]
    top_contexts = df_all.iloc[top_indices]["cleaned_text"].tolist()

    # --- Buat prompt untuk LLM ---
    context = "\n".join([f"- {c}" for c in top_contexts])
    prompt = dedent(f"""
    Konteks berikut diambil dari beberapa sumber data internal:
    {context}

    Berdasarkan konteks di atas, jawab pertanyaan berikut dengan jelas dan ringkas.
    Pertanyaan pengguna: "{query}"
    Jawaban:
    """)

    # --- Panggil Gemini ---
    response = model_llm.generate_content(prompt)
    return response.text.strip()


