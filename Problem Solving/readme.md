

# **Deteksi Kecurangan Reimbursement dengan AI/ML**

Proyek ini mengusulkan solusi untuk mendeteksi dan mencegah aktivitas kecurangan pada proses *reimbursement* internal perusahaan menggunakan teknologi **Machine Learning (ML)**.

---

### **1. Solusi AI/ML yang Diusulkan**

Kami mengusulkan penggunaan **Graph Neural Networks (GNN)**, sebuah model AI berbasis grafik. Alih-alih hanya menganalisis satu transaksi secara terisolasi, model ini melihat seluruh data perusahaan—karyawan, nota, dan vendor—sebagai sebuah **jaringan raksasa**.

* **Node (Titik):** Setiap karyawan, nota, dan vendor adalah titik dalam jaringan.
* **Edge (Garis Penghubung):** Hubungan antar titik, seperti "karyawan A mengajukan nota B," adalah garis penghubung.

Model ini sangat efektif karena mampu mengenali pola-pola kecurangan yang lebih canggih, seperti:

* **Kolusi:** Mendeteksi sekelompok karyawan yang berulang kali mengajukan *reimbursement* dari vendor yang sama.
* **Vendor Palsu:** Mengidentifikasi vendor yang baru muncul dan tiba-tiba digunakan oleh banyak karyawan yang tidak saling berhubungan.

---

### **2. Data yang Diperlukan**

Untuk melatih dan menerapkan model ini, diperlukan data historis dari sistem *reimbursement* perusahaan.

* **Data Karyawan:** ID, departemen.
* **Data Nota:** ID nota, jumlah, kategori pengeluaran, lokasi.
* **Data Vendor:** Nama vendor, lokasi.
* **Data Hubungan (Relationship):** Catatan yang menghubungkan karyawan dengan nota, dan nota dengan vendor.

---

### **3. Cara Penerapan dan Infrastruktur**

#### **Cara Penerapan**

1.  **Pengumpulan Data:** Mengintegrasikan data dari sistem internal (misalnya, ERP atau *platform reimbursement*).
2.  **Pembentukan Grafik:** Mengubah data mentah menjadi struktur grafik (misalnya, menggunakan pustaka seperti `NetworkX` di Python).
3.  **Pelatihan Model GNN:** Melatih model untuk mengenali pola kecurangan yang sudah terjadi di masa lalu.
4.  **Integrasi API:** Membuat *endpoint* API yang menerima data pengajuan baru dari sistem *reimbursement*.
5.  **Analisis Real-Time:** Setiap pengajuan baru akan dianalisis oleh model GNN. Jika model mendeteksi adanya pola mencurigakan dalam jaringan, pengajuan akan ditandai dengan **skor risiko tinggi** dan dikirim ke tim audit untuk verifikasi manual.

#### **Infrastruktur Minimal**

* **Server Komputasi:** Diperlukan server dengan spesifikasi minimum:
    * **CPU:** 4-core
    * **RAM:** 16-32 GB
    * **GPU:** Rekomendasi untuk mempercepat pelatihan model.
* **Lingkungan Pemrograman:** Python dengan pustaka-pustaka seperti **PyTorch**/**TensorFlow**, **Scikit-learn**, **Pandas**, dan **PyG (PyTorch Geometric)**.
* **Database:** Basis data yang dapat menyimpan data dalam format grafik atau yang mudah diubah ke format tersebut (misalnya, PostgreSQL atau Neo4j).

---
