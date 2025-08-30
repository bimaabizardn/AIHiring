# Proyek Klasifikasi Teks Layanan Pelanggan

Proyek ini bertujuan untuk membangun model klasifikasi teks sederhana yang dapat mengkategorikan pertanyaan pelanggan ke dalam beberapa label yang telah ditentukan: `Problem`, `Information`, dan `Request`. Model ini dilatih menggunakan dataset yang berisi percakapan layanan pelanggan yang sudah diberi label.

---

## Panduan Instalasi

Ikuti langkah-langkah di bawah ini untuk menyiapkan lingkungan proyek Anda.

1.  **Kloning Repositori**


2.  **Buat Lingkungan Virtual (Opsional, tapi Sangat Direkomendasikan)**
    ```
    python -m venv venv
    ```

3.  **Aktifkan Lingkungan Virtual**
    * **Pada macOS dan Linux:**
        ```
        source venv/bin/activate
        ```
    * **Pada Windows:**
        ```
        .\venv\Scripts\activate
        ```

4.  **Instal Dependensi**
    Instal semua pustaka yang diperlukan dari file `requirements.txt`:
    ```
    pip install -r requirements.txt
    ```

---

## Alur Kerja Proyek

1.  **Pembersihan dan Pra-pemrosesan Data**
    Proses ini dijelaskan secara rinci dalam file `data_preprocessing.ipynb`. Notebook ini menangani format data yang tidak konsisten, membersihkan teks, dan mengubah label menjadi format numerik.

2.  **Pelatihan dan Evaluasi Model**
    Notebook `model_training.ipynb` berisi kode untuk melatih model klasifikasi (SVM) menggunakan data yang telah dipreproses. Notebook ini juga mencakup evaluasi performa model menggunakan metrik seperti akurasi, presisi, dan recall.

3.  **Penggunaan Model**
    Skrip `predict.py` di dalam folder `src/` adalah modul utama untuk melakukan prediksi pada teks baru. Skrip ini memuat model dan vectorizer yang sudah dilatih dari direktori `models/` dan siap untuk digunakan.

---

## Cara Penggunaan

Setelah lingkungan Anda siap, Anda dapat menjalankan skrip prediksi dari terminal:

Skrip ini akan memuat model yang sudah dilatih dan memberikan contoh prediksi.

---

## Cara Menggunakan Model sebagai API/Modul

Anda juga dapat mengimpor fungsi `predict_label` dari `predict.py` ke dalam skrip Python lain untuk integrasi yang lebih mudah.

Berikut adalah contoh cara menggunakannya:

`from src.predict import predict_label`

# Teks yang ingin Anda prediksi
teks_baru = ["internet saya putus, tolong perbaiki", "apakah ada paket promo terbaru?", "saya ingin pasang baru"]

# Panggil fungsi predict_label untuk mendapatkan prediksi
prediksi_hasil = predict_label(teks_baru)

# Cetak hasilnya
for teks, hasil in zip(teks_baru, prediksi_hasil):
    print(f"Teks: '{teks}' -> Prediksi: {hasil}")

