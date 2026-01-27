# Implementasi Weighted Naive Bayes untuk Klasifikasi Tingkat Kematangan Buah Kelapa Sawit Berbasis Citra Digital

## Deskripsi
Repository ini berisi implementasi metode **Naive Bayes** dan **Weighted Naive Bayes** untuk melakukan klasifikasi tingkat kematangan buah kelapa sawit menggunakan citra digital.  
Aplikasi dikembangkan dalam bentuk **aplikasi web berbasis Flask (Python)** sebagai bagian dari penelitian skripsi.

---

## Tujuan Penelitian
1. Mengimplementasikan metode Naive Bayes dan Weighted Naive Bayes pada klasifikasi citra buah kelapa sawit.
2. Membandingkan performa metode Naive Bayes dengan Weighted Naive Bayes.
3. Membangun aplikasi web untuk melakukan pengujian citra secara langsung.

---

## Kelas Klasifikasi
Klasifikasi tingkat kematangan buah kelapa sawit dibagi menjadi tiga kelas:
- Matang  
- Terlalu Matang  
- Tidak Matang  

---

## Metode dan Pendekatan
- Ekstraksi fitur menggunakan **Histogram Warna (RGB)**
- Algoritma klasifikasi:
  - Naive Bayes
  - Weighted Naive Bayes
- Evaluasi performa model menggunakan nilai akurasi

---

## Alur Sistem
1. Pengguna mengunggah citra buah kelapa sawit melalui antarmuka web.
2. Sistem melakukan praproses citra dan ekstraksi fitur histogram warna.
3. Fitur citra digunakan sebagai input ke model Naive Bayes dan Weighted Naive Bayes.
4. Sistem menghitung probabilitas posterior untuk setiap kelas.
5. Hasil klasifikasi tingkat kematangan ditampilkan kepada pengguna.

---

## Teknologi yang Digunakan
- Python
- Flask
- OpenCV
- NumPy
- Scikit-learn
- HTML dan CSS

---

## Struktur Direktori
web_app/
├── app.py
├── static/
├── templates/
├── oil_palm/ (dataset – tidak disertakan di repository)
└── .gitignore


---

## Informasi Dataset
Dataset citra buah kelapa sawit **tidak disertakan dalam repository ini**.  
Dataset digunakan khusus untuk keperluan penelitian dan pengujian model secara lokal guna menjaga privasi data dan etika penelitian.

Struktur dataset pada lingkungan lokal:
oil_palm/
├── matang/
├── terlalu_matang/
└── tidak_matang/


---

## Cara Menjalankan Aplikasi
1. Pastikan Python telah terinstal pada sistem
2. Install dependensi yang diperlukan
3. Jalankan aplikasi dengan perintah:
```bash
python app.py
Akses aplikasi melalui browser:

http://localhost:5000
Hasil Penelitian
Hasil pengujian menunjukkan bahwa metode Weighted Naive Bayes memberikan performa yang lebih baik dibandingkan metode Naive Bayes standar dalam mengklasifikasikan tingkat kematangan buah kelapa sawit berbasis citra digital.

Penulis
Nama : Refriyan
Program : (Informatika)
Institusi : (Itenas)
Tahun : 2024