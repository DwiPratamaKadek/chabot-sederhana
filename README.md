#   

## Run Project 
1. Cara pertama 
```bash 
    fastapi dev main.py
```
2. Cara kedua 
```bash 
    uvicorn main:app --reload
```

# Penjelasan tentang project 
## Pengembangan Chatbot Hybrid Berbasis Gabungan TF-IDF dan Semantic Embedding dengan LLM Gemini untuk Pembangkitan Teks

### Apa itu Retrievel ? 
### Apa itu TF - IDF ? 
### Apa itu Cosine Similarity ?  


### Tahapan Pembuatan Chatbot Sederhana.

| Langkah                                  | Keterangan                            |
| ---------------------------------------- | ------------------------------------- | 
| 1️⃣ Siapkan dataset (scraping Wikipedia) | Gunakan BeautifulSoup                 | 
| 2️⃣ Preprocessing teks                   | Bersihkan teks pakai regex + Sastrawi | 
| 3️⃣ TF-IDF Vectorizer                    | Ubah teks jadi angka                  | 
| 4️⃣ Cosine Similarity                    | Cari dokumen paling mirip             | 
| 5️⃣ Simpan model                         | joblib                                | 
| 6️⃣ Integrasi API                        | FastAPI / Flask                       | 

#### Package yang di perlukan 

| Package          | Kegunaan                              |
| ---------------- | ------------------------------------- |
| `pandas`         | Untuk membaca/menyimpan data scraping |
| `beautifulsoup4` | Untuk scraping HTML                   |
| `requests`       | Untuk mengambil halaman web           |
| `scikit-learn`   | Untuk TF-IDF dan cosine similarity    |
| `Sastrawi`       | Untuk stemming bahasa Indonesia       |

#### Tools tambahan 

| Tools             | Kegunaan                              |
| ----------------  | ------------------------------------- |
| Anaconda          | Biar bisa make conda promt            |
| Conda Promt       | Biar bisa buat env sendiri            |


#### Set Up Pertama

1. Membuat ENV pada conda promt
```bash 
    conda create -n chatbot-env python=3.10
```

2. Activare env 
```bash 
    conda activate chatbot-env
```
3. Install Package 
```bash 
    conda install jupyter pandas scikit-learn beautifulsoup4
    pip install Sastrawi
```
4. Coding lah 

```bash 
    project/
├── scraping/
│   ├── data_all.csv
├── preprocessing/
│   ├── clean_text.py      ← berisi fungsi cleaning
│   ├── clean_dataset.py   ← batch cleaning (yang kamu buat)
├── chatbot/
│   ├── chatbot_tfidf.py   ← untuk TF-IDF + matching

```

## Evaluasi 
1. Jika Pake Anaconda Promt pake buat env di wajibkan buatlah envnya di derecotry dari folder root projectnya biar gak ribet tar.  
