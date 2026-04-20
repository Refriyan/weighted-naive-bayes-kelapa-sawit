# 🌴 Implementasi Weighted Naive Bayes untuk Klasifikasi Kematangan Buah Kelapa Sawit

## 📌 Deskripsi

Proyek ini merupakan implementasi metode **Naive Bayes** dan **Weighted Naive Bayes** untuk mengklasifikasikan tingkat kematangan buah kelapa sawit berbasis **citra digital**.

Aplikasi dikembangkan dalam bentuk **web application menggunakan Flask (Python)** sebagai bagian dari penelitian skripsi.


## 🎯 Tujuan Penelitian

* Mengimplementasikan algoritma **Naive Bayes** dan **Weighted Naive Bayes**
* Menganalisis performa kedua metode dalam klasifikasi citra
* Membangun aplikasi berbasis web untuk pengujian secara langsung


## 🧪 Kelas Klasifikasi

Sistem mengklasifikasikan buah kelapa sawit ke dalam 3 kategori:

* ✅ Matang
* ⚠️ Terlalu Matang
* ❌ Tidak Matang


## ⚙️ Metode dan Pendekatan

### 🔍 Ekstraksi Fitur

* Histogram warna berbasis **RGB**

### 🧠 Algoritma

* Naive Bayes
* Weighted Naive Bayes

### 📊 Evaluasi

* Akurasi klasifikasi sebagai metrik utama

## 🔄 Alur Sistem

1. User mengunggah citra buah kelapa sawit
2. Sistem melakukan preprocessing citra
3. Ekstraksi fitur menggunakan histogram RGB
4. Model menghitung probabilitas posterior
5. Sistem menentukan kelas kematangan
6. Hasil ditampilkan ke user

---

## 🧰 Teknologi yang Digunakan

* Python
* Flask
* OpenCV
* NumPy
* Scikit-learn
* HTML & CSS

---

## 📁 Struktur Proyek

```
web_app/
├── app.py
├── static/
├── templates/
├── oil_palm/        # dataset (tidak disertakan)
└── .gitignore
```

---

## 📊 Dataset

Dataset citra **tidak disertakan dalam repository** karena:

* Digunakan untuk keperluan penelitian
* Menjaga privasi dan etika penggunaan data

Struktur dataset lokal:

```
oil_palm/
├── matang/
├── terlalu_matang/
└── tidak_matang/
```

---

## 🚀 Cara Menjalankan Aplikasi

1. Pastikan Python sudah terinstall
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan aplikasi:

   ```bash
   python app.py
   ```
4. Buka di browser:

   ```
   http://localhost:5000
   ```

---

## 📈 Hasil Penelitian

Metode **Weighted Naive Bayes** menunjukkan performa yang lebih baik dibandingkan **Naive Bayes standar**, terutama dalam menangani ketidakseimbangan data pada klasifikasi tingkat kematangan buah kelapa sawit.

---

## 👨‍🎓 Penulis

* **Nama**: Refriyan Adrianto
* **Program Studi**: Informatika
* **Institusi**: Institut Teknologi Nasional (Itenas)
* **Tahun**: 2024

---

<img width="4960" height="7016" alt="Poster_page-0001" src="https://github.com/user-attachments/assets/2bc89b56-88c3-4f37-b1a5-e9d01f86752e" />

## 📌 Catatan

Proyek ini dikembangkan untuk keperluan akademik dan dapat digunakan sebagai referensi untuk:

* Machine Learning pada citra digital
* Klasifikasi berbasis probabilistik
* Implementasi Weighted Naive Bayes
