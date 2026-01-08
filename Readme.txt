# TUGAS BESAR KECERDASAN BUATAN - SISTEM FUZZY (MODEL SUGENO)
# Judul: Sistem Rekomendasi Kursus Udemy Berdasarkan Kualitas dan Harga

Link Repositori: https://github.com/ardiannafissamudra/Fuzzy-System-Udemy-Recommendation

## 1. Identitas Kelompok & Pembagian Tugas
1. Ardian Nafis Samudra (103132400012)
   - Peran: Implementasi Kode Program (Python), Pre-processing Data, dan Integrasi GitHub.
   
2. Abdullah Ahmad Izzah (103132430024)
   - Peran: Analisis Aturan Fuzzy (Rule Base), Riset Dataset, dan Desain Poster A3.

## 2. Deskripsi Proyek
Proyek ini menggunakan Logika Fuzzy Model Sugeno untuk menentukan kursus terbaik dari platform Udemy. 
Sistem ini memproses data riil dari dataset 'udemy_courses.csv' dengan kriteria:
- Input 1: Kualitas (Diambil dari normalisasi jumlah ulasan/num_reviews).
- Input 2: Harga (Diambil dari normalisasi harga kursus/price).
- Output: Skor Kelayakan (Skala 0-100).

Metode Defuzzifikasi yang digunakan adalah Weighted Average (Rata-rata Terbobot).

## 3. Struktur File
- main.py: Script Python utama untuk menjalankan perhitungan fuzzy.
- udemy_courses.csv: Dataset asli berisi daftar kursus Udemy.
- peringkat_udemy.csv: File hasil output yang berisi daftar kursus yang sudah diranking.
- Readme.txt: Dokumen panduan dan identitas kelompok.

## 4. Cara Menjalankan Program
1. Pastikan Python 3.x sudah terinstal di komputer Anda.
2. Letakkan file 'main.py' dan 'udemy_courses.csv' dalam folder yang sama.
3. Buka terminal atau command prompt di folder tersebut.
4. Jalankan perintah: python main.py
5. Hasil peringkat akan muncul di layar dan tersimpan otomatis di file 'peringkat_udemy.csv'.
