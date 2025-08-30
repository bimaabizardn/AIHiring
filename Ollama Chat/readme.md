Deskripsi:
Proyek ini mengimplementasikan antarmuka chat berbasis web menggunakan Python dan framework Streamlit, yang berintegrasi langsung dengan model AI "gemma3:1b" dari Ollama. Antarmuka ini memungkinkan pengguna untuk mengirimkan pertanyaan teks dan menerima jawaban yang dihasilkan oleh model AI secara real-time.

Metode yang Digunakan:
- Streamlit: Digunakan untuk membangun antarmuka pengguna (UI) yang sederhana dan interaktif.
- Ollama Model: Model gemma:2b adalah model bahasa besar yang diunduh dan dijalankan secara lokal oleh Ollama untuk menghasilkan respons.

Alur Kode (`app.py`):
1.  **Inisialisasi**: Skrip menginisialisasi Streamlit dan mencoba membuat koneksi ke Ollama Client. Status koneksi disimpan.
2.  **Manajemen Riwayat**: Riwayat percakapan disimpan dalam `st.session_state` sehingga pesan tidak hilang saat halaman di-refresh.
3.  **Input Pengguna**: Pengguna memasukkan pertanyaan melalui `st.chat_input`.
4.  **Menampilkan Pesan**: Setiap pesan pengguna dan respons AI ditampilkan dalam format chat (`st.chat_message`).
5.  **Pemanggilan Model**: Ketika pengguna mengirim pertanyaan, skrip akan memanggil Ollama API dengan mengirimkan seluruh riwayat percakapan untuk mempertahankan konteks.
6.  **Streaming Respon**: Respons dari model di-stream secara bertahap menggunakan `st.write_stream` untuk pengalaman pengguna yang lebih baik.

Langkah Instalasi dan Testing:
1.  **Install Ollama**: Unduh dan instal Ollama dari [https://ollama.com](https://ollama.com).
2.  **Jalankan Ollama**: Pastikan Ollama berjalan di latar belakang.
3.  **Unduh Model**: Buka terminal dan unduh model gemma:2b dengan perintah:
    ```
    ollama pull gemma:2b
    ```
4.  **Buat Lingkungan Virtual**: Buka folder proyek di VS Code dan buat lingkungan virtual baru.
    ```
    python -m venv venv
    ```
5.  **Aktifkan Lingkungan Virtual**:
    - Windows: `.\venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`
6.  **Instal Dependensi**: Instal pustaka yang diperlukan dari `requirements.txt`.
    ```
    pip install -r requirements.txt
    ```
7.  **Jalankan Aplikasi**: Jalankan aplikasi Streamlit dengan perintah:
    ```
    streamlit run app.py
    ```
    Aplikasi chat akan terbuka di browser web Anda, dan Anda siap menggunakannya.
