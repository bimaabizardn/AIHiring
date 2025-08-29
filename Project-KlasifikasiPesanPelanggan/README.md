# Proyek Klasifikasi Teks Layanan Pelanggan

Proyek ini bertujuan untuk membangun model klasifikasi teks sederhana yang dapat mengkategorikan pertanyaan pelanggan ke dalam beberapa label yang telah ditentukan: `Problem`, `Information`, dan `Request`. Model ini dilatih menggunakan dataset yang berisi percakapan layanan pelanggan yang sudah diberi label.

---

## Panduan Instalasi

Ikuti langkah-langkah di bawah ini untuk menyiapkan lingkungan proyek Anda.

1.  **Kloning Repositori**
    ```
    git clone <URL_repositori_Anda>
    cd <nama_folder_repositori>
    ```

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
