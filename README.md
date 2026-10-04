# 🧮 MathQuiz – Quiz Matematika

Aplikasi web quiz matematika sederhana untuk membantu anak belajar dan menghafal operasi hitung dasar. Dibuat dengan **Python** dan **Streamlit**, nyaman dibuka lewat smartphone.

🔗 **Coba langsung:** https://mathquiz-wedhasmoro.streamlit.app/

## ✨ Fitur

- 5 jenis operasi: penjumlahan, pengurangan, perkalian, pembagian, dan campuran
- 3 tingkat kesulitan: Mudah, Sedang, Sulit
- Pilihan jumlah soal: 5, 10, atau 20
- Soal dibuat acak, 4 pilihan jawaban (A-D)
- Feedback langsung (benar/salah), skor, dan progress soal
- Halaman hasil berisi nilai dan pesan motivasi
- Tampilan mobile friendly

## 🎯 Rentang Angka per Level

| Level | Penjumlahan / Pengurangan | Perkalian | Pembagian |
|---|---|---|---|
| Mudah | 1 – 20 | 1–5 × 1–10 | hasil 1–10, pembagi 2–5 |
| Sedang | 10 – 100 | 2–9 × 2–12 | hasil 2–12, pembagi 2–9 |
| Sulit | 100 – 999 | 11–25 × 3–15 | hasil 5–25, pembagi 6–15 |

Soal pembagian dibuat dari hasil kali, sehingga selalu menghasilkan bilangan bulat.

## 🛠️ Teknologi

- Python 3.11+
- Streamlit

## 🚀 Menjalankan di Komputer Sendiri

```bash
# 1. Clone repository
git clone <URL repository GitHub kamu>
cd mathquiz

# 2. Buat dan aktifkan virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

# 3. Install library
pip install -r requirements.txt

# 4. Jalankan aplikasi
streamlit run app.py
```

Buka `http://localhost:8501` di browser.

## 🧪 Menjalankan Tes

```bash
python test_quiz.py
```

## 📁 Struktur Project

```
mathquiz/
├── .streamlit/config.toml   # pengaturan tema
├── app.py                   # tampilan dan alur quiz (Streamlit)
├── quiz.py                  # pembuat soal dan pilihan jawaban
├── style.css                # styling tampilan
├── test_quiz.py             # tes otomatis
├── requirements.txt         # daftar library
└── README.md
```

## 🗺️ Rencana Pengembangan

- [ ] Timer dan efek suara
- [ ] Riwayat quiz
- [ ] Profil pengguna dan leaderboard (database)
- [ ] Tingkat kesulitan adaptif

## 👤 Pembuat

Raditya Suryo Wedhasmoro – Informatika, Universitas Gunadarma
