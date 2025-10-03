import math

class ColumnarTransposition:
    def __init__(self, key):
        """
        Inisialisasi cipher dengan kunci (urutan kolom, e.g., '4312').
        
        Args:
            key (str): Kunci berupa string angka.
        """
        self.key_str = key
        # Buat daftar urutan pembacaan kolom (index 0-based)
        # Kunci '4312' berarti kolom 1 akan dibaca pertama, kolom 2 kedua, dst.
        # Kolom '1' di kunci adalah kolom ke-2 (index 2) di matriks.
        self.key_order = self._get_key_order(key) # Contoh: [2, 3, 1, 0] untuk '4312'
        self.num_cols = len(key)

    def _get_key_order(self, key):
        """
        Mengubah kunci string menjadi urutan index kolom (0-based) untuk pembacaan.
        Contoh: '4312' -> [2, 3, 1, 0] (Kolom ke-3, ke-4, ke-2, ke-1 akan dibaca)
        """
        # Angka di kunci adalah 1-based, index di Python adalah 0-based
        # Buat pasangan (angka kunci, index kolom)
        indexed_key = [(int(k), i) for i, k in enumerate(key)]
        
        # Urutkan berdasarkan angka kunci (4312 -> 1, 2, 3, 4)
        indexed_key.sort(key=lambda x: x[0])
        
        # Ambil urutan index kolom yang sesuai dengan urutan pembacaan
        # Kolom dengan angka '1' di kunci dibaca pertama, dst.
        return [item[1] for item in indexed_key] # Index kolom dalam matriks

    def encrypt(self, plaintext, padding_char='X'):
        """
        Melakukan enkripsi Columnar Transposition.
        
        Args:
            plaintext (str): Teks asli yang akan dienkripsi.
            padding_char (str): Karakter yang digunakan untuk mengisi sisa.
            
        Returns:
            str: Ciphertext hasil enkripsi.
        """
        P = plaintext.replace(" ", "").upper()
        
        # 1. Tentukan dimensi
        num_rows = math.ceil(len(P) / self.num_cols)
        
        # 2. Tambahkan padding jika perlu
        P_len_padded = num_rows * self.num_cols
        P += padding_char * (P_len_padded - len(P))
        
        # 3. Susun Matriks (secara horizontal)
        matrix = [
            list(P[i:i + self.num_cols]) 
            for i in range(0, len(P), self.num_cols)
        ]
        
        # 4. Baca Kolom Berdasarkan Kunci
        ciphertext = ""
        # self.key_order menentukan urutan kolom mana yang harus dibaca
        for col_index in self.key_order:
            for row in matrix:
                ciphertext += row[col_index]
                
        return ciphertext

    def decrypt(self, ciphertext):
        """
        Melakukan dekripsi Columnar Transposition.
        
        Args:
            ciphertext (str): Teks terenkripsi.
            
        Returns:
            str: Plaintext hasil dekripsi (mungkin termasuk padding).
        """
        C = ciphertext
        C_len = len(C)
        
        # 1. Tentukan dimensi
        if C_len % self.num_cols != 0:
            # Seharusnya tidak terjadi jika enkripsi dilakukan dengan benar
            raise ValueError("Panjang ciphertext tidak valid.")
            
        num_rows = C_len // self.num_cols
        
        # 2. Tentukan panjang setiap kolom
        # Dalam implementasi sederhana ini, semua kolom memiliki panjang yang sama
        col_length = num_rows
        
        # 3. Susun Matriks (secara vertikal)
        # Inisialisasi matriks kosong (ukuran num_rows x self.num_cols)
        matrix = [['' for _ in range(self.num_cols)] for _ in range(num_rows)]
        
        c_pointer = 0 # Penunjuk posisi di ciphertext
        
        # Isi kolom berdasarkan urutan kunci (self.key_order)
        for col_index_to_fill in self.key_order:
            # Ambil 'col_length' karakter dari ciphertext
            column_data = C[c_pointer:c_pointer + col_length]
            
            # Isi kolom yang bersangkutan di matriks
            for row in range(num_rows):
                matrix[row][col_index_to_fill] = column_data[row]
                
            c_pointer += col_length # Majukan pointer
            
        # 4. Baca Baris Demi Baris
        plaintext = ""
        for row in matrix:
            plaintext += "".join(row)
            
        # Catatan: Padding harus dihilangkan di luar fungsi ini jika diperlukan
        return plaintext

# --- Contoh Penggunaan ---

# Input:
plaintext_input = "Implementasikan Columnar Transposition Cipher"
key_input = "4312567"

# Inisialisasi
cipher = ColumnarTransposition(key_input)

# ENKRIPSI
ciphertext_result = cipher.encrypt(plaintext_input, padding_char='Z')

# DEKRIPSI
# Catatan: Hasil dekripsi masih mengandung karakter padding 'Z'
decrypted_result_with_padding = cipher.decrypt(ciphertext_result)

# Menghilangkan padding (asumsi padding adalah 'Z' dan hanya ada di akhir)
decrypted_result = decrypted_result_with_padding.rstrip('Z')

print("=== Columnar Transposition Cipher ===")
print(f"Plaintext Asli: {plaintext_input}")
print(f"Kunci: {key_input}")
print("-" * 35)
print(f"Ciphertext: {ciphertext_result}")
print(f"Plaintext Dekripsi: {decrypted_result}")
print("-" * 35)

# --- Contoh Kedua (Untuk membandingkan dengan contoh penjelasan) ---
print("\n=== Contoh Kedua (Kunci Pendek) ===")
cipher2 = ColumnarTransposition("4312")
pt2 = "INIMENCOBAENKRIPSI"
ct2 = cipher2.encrypt(pt2, padding_char='X')
dt2 = cipher2.decrypt(ct2).rstrip('X')

print(f"Plaintext Asli: {pt2}")
print(f"Kunci: 4312")
print(f"Ciphertext: {ct2}")
print(f"Plaintext Dekripsi: {dt2}")