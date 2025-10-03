# 🔒 Columnar Transposition Cipher (Implementasi Python)
## 📜 Deskripsi Proyek
Proyek ini adalah implementasi Python dari Columnar Transposition Cipher, sebuah metode kriptografi klasik yang termasuk dalam kategori transposisi (mengubah urutan karakter, bukan karakter itu sendiri). Program ini memungkinkan pengguna untuk mengenkripsi dan mendekripsi pesan dengan menentukan panjang kunci (jumlah kolom), di mana kunci urutan kolom akan dibuat secara acak dan unik secara otomatis.

## ✨ Fitur Utama
- Enkripsi dan Dekripsi: Fungsi lengkap untuk mengubah plaintext menjadi ciphertext dan mengembalikannya.
- Kunci Otomatis: Kunci urutan kolom (permutasi angka) dihasilkan secara otomatis berdasarkan panjang yang dimasukkan pengguna.
- Penanganan Spasi: Spasi diabaikan (ignored) dan semua teks dikonversi menjadi huruf kapital (uppercase) sebelum enkripsi.
- Padding Otomatis: Menambahkan karakter padding (default: 'Z') jika panjang plaintext tidak pas mengisi matriks kolom.

## 🚀 Instalasi dan Penggunaan
1. Prasyarat
Anda hanya perlu Python 3.x terinstal pada sistem Anda.
2. Menjalankan Program
- Salin (atau clone) repositori ini ke komputer lokal Anda.
- Buka terminal atau command prompt dan navigasikan ke direktori proyek.
- Jalankan skrip main():

      `python nama_file_anda.py # (Ganti nama_file_anda.py dengan nama file Python Anda, misalnya columnar_cipher.py)`

3. Interaksi Program
Program akan meminta Anda untuk memasukkan dua hal secara berurutan:

    - Plaintext: Teks yang ingin Anda enkripsi.
    
    - Panjang Kunci (Jumlah Kolom): Angka yang menentukan lebar matriks (grid). Program akan menghasilkan kunci urutan acak berdasarkan panjang ini.

## ⚙️Output

<img width="469" height="217" alt="image" src="https://github.com/user-attachments/assets/e21528cd-6ddd-43eb-94a5-4d47010d8213" />
