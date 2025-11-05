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

### Apa itu Retrieval ? 
Retrival itu mengambil dan mencari potongan kata dari suatu paragraf,kalimat, dll. 
Gampangnya Retrival itu mencari kalimat yang benar benar cocok atau sama dari apa yang kita cari, contohnya : "apa itu TF-IDF" Retrival akan mencocokan dan membandingkan makna atau isi dari kata, kemudian akan di tampilkan yang mana kata mirip.

### Apa itu Reranking ? 
Reranking maknanya itu mencari berdasarkan maknanya, dimana Reranking mengurutkan ulang kembali dari hasil Retrieval. 
Gampangnya Reranking ini mengurutkan kembali lagi apa sudah dicari oleh Retrieval dan Reranking ini akan memeriksa ulang satu persatu, mencocokan lagi berdasarkan makna,mengurutkan kembali lagi mana yang lebih relevan dari pertanyaan. 

### Apa itu TF - IDF ? 
TF-IDF itu adalah alat yang digunakan buat melakukan Retrieval.
TF-IDF (Term Frequency Inverse Document Frequency) yang dimana tool membantu komputer untuk mengerti kata mana yang penting.
Jadi gampangnya TF-IDF itu ngebantu komputer mengetahui seberapa sering kata itu muncul dan seberapa jarang ada kata itu di kalimat lain. 

### Nah gimana cara kerja TF-IDF ? 
 1. TF-IDF akan memecahkan kalimat menjadi kata "aku tadi makan siang, tapi lupa sarapan" ["aku", "tadi", "makan", "siang", "tapi", "lupa", "sarapan"]
 2. Kemudian akan menghitung TFnya dimana TF akan menghitung dan mencari kata yang paling sering muncul(yang penting) kata "makan" = 1 kata itu muncul 2 x pada kalimat, jadi TF = 1/2 = 0,5. yaa 
 3. Kemudian akan menghitung juga yang jarang muncul(yang tidak penting) 
 ini rumusnya 
 ```bash 
    IDF = log(total dokumen / dokumen yang mengandung kata itu)
 ```
 4. Kemudian akan di gabungkan TF x IDF 
 5. Kemudian hasil dari perhitungan TF-IDF akan diubah menjadi vektor berdasarkan nilai dari TF-IDFnya, jadinya komputer mudah mengukur kemiripan dari setiap kata(tool yang bisanya buat ngebandingin make ***cosine similarity***)
 6. Kata yang sering muncul di dokumen tertentu tapi jarang di dokumen lain → skor tinggi (penting),
Kata yang muncul di semua dokumen → skor rendah (nggak penting)
**Yaa kurang lebih kek gitu**


### Apa itu Semantic Embedding ? 
### Apa itu Cosine Similarity ?  
### Apa itu LLM ? 
### Kenapa menggabungkan TF-IDF dengan Semantic Embedding ? 
### Kenapa menggunakan LLM sebagai generate textnya ? 

***belum tak jawab bang masih malas***

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
