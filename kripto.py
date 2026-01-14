import streamlit as st
import pandas as pd

st.set_page_config(page_title="Modifikasi Kriptografi", page_icon="🔒", layout="wide")

# Judul aplikasi
st.title("🔒 MODIFIKASI KRIPTOGRAFI BERBASIS POLA WARNA IKAN CUPANG")
st.write("Oleh: GILANG YUDHA PRAJATMA - 24.83.1060")

st.markdown("---")

# Tampilkan informasi proyek
with st.expander("📋 Tentang Proyek Ini"):
    st.markdown("""
    **Modifikasi kriptografi menggunakan pola warna ikan cupang** merupakan pendekatan inovatif yang menggabungkan ilmu 
    keamanan informasi dan karakteristik biologis. Dengan pemanfaatan pola warna yang unik dan kompleks, metode ini 
    berpotensi meningkatkan keamanan data serta membuka peluang pengembangan kriptografi berbasis biomimetik di masa depan.
    
    Ikan cupang memiliki pola warna yang sangat beragam, mulai dari kombinasi merah, biru, putih, hitam, hingga gradasi 
    warna yang kompleks. Setiap ikan cupang memiliki pola warna yang unik dan sulit direplikasi, sehingga pola ini dapat 
    dimanfaatkan sebagai sumber kunci dalam sistem kriptografi.
    """)

# Tabel Alphabet sesuai dengan dokumen
st.subheader("📊 TABEL ALPHABET")

alphabet_data = {
    'Huruf': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    'Kode': ['avt', 'gor', 'mc', 'cl', 'bgl', 'mrl', 'hlb', 'fcp', 'sr', 'ki', 
             'giz', 'blc', 'wp', 'oa', 'pnd', 'nm', 'fnc', 'nc', 'Cpr', 'kg', 
             'kc', 'ylo', 'rd', 'b', 'vol', 'yd'],
    'Nama Pola': ['Avatar', 'Gordon', 'Multi color', 'Celo', 'Besgel', 'Marbel', 
                  'hellboy', 'fccp', 'Super red', 'koi', 'grizzle', 'black', 
                  'White platinum', 'oranye', 'Panda', 'Nemo', 'fancy', 'Nemo cooper', 
                  'Copper', 'Koi galaxy', 'Koi candy', 'Yellow', 'Red dragon', 
                  'Blue', 'Violet', 'Yellow dragon']
}

df_alphabet = pd.DataFrame(alphabet_data)

# Tampilkan tabel dalam 2 kolom seperti di dokumen
col1, col2 = st.columns(2)

with col1:
    st.write("**A - N**")
    st.dataframe(df_alphabet.iloc[:14][['Huruf', 'Kode', 'Nama Pola']], use_container_width=True, hide_index=True)

with col2:
    st.write("**O - Z**")
    st.dataframe(df_alphabet.iloc[14:][['Huruf', 'Kode', 'Nama Pola']], use_container_width=True, hide_index=True)

# Buat dictionary untuk mapping
huruf_to_kode = {row['Huruf']: row['Kode'] for _, row in df_alphabet.iterrows()}
kode_to_huruf = {row['Kode']: row['Huruf'] for _, row in df_alphabet.iterrows()}
huruf_list = list(huruf_to_kode.keys())
kode_list = list(huruf_to_kode.values())

st.markdown("---")

# Aturan penggunaan
st.subheader("📝 ATURAN PENGGUNAAN")
st.markdown("""
1. **Satu huruf plaintext digeser dengan satu angka pada digit key**
2. **Pergeseran mengarah ke kanan**
3. **Bila pergeseran ke kanan sudah mentok sisi kanan maka dilanjutkan dari sisi kiri dengan baris di bawahnya**
4. **Plaintext lebih panjang daripada key maka key diulang**
5. **Key maksimal 5 angka**
""")

# Fungsi untuk enkripsi
def encrypt_four_square_cipher(plaintext, key):
    """
    Implementasi modifikasi Four Square Cipher dengan tabel alphabet khusus
    """
    # Bersihkan input
    plaintext = plaintext.upper().replace(" ", "")
    
    # Validasi input hanya huruf A-Z
    if not all(c in huruf_to_kode for c in plaintext):
        st.error("Error: Plaintext hanya boleh berisi huruf A-Z (tanpa spasi atau karakter khusus)")
        return ""
    
    # Validasi key
    key_str = str(key).replace(" ", "")
    if not all(c.isdigit() for c in key_str):
        st.error("Error: Key hanya boleh berisi angka")
        return ""
    
    if len(key_str) > 5:
        st.error("Error: Key maksimal 5 angka")
        return ""
    
    # Konversi key ke list angka
    key_digits = [int(d) for d in key_str]
    
    # Inisialisasi ciphertext
    ciphertext_codes = []
    
    # Proses enkripsi per huruf
    for i, char in enumerate(plaintext):
        # Dapatkan key digit untuk huruf ini (dengan pengulangan jika perlu)
        key_digit = key_digits[i % len(key_digits)]
        
        # Dapatkan indeks huruf dalam alphabet
        char_index = huruf_list.index(char)
        
        # Hitung indeks baru dengan pergeseran
        new_index = (char_index + key_digit) % len(huruf_list)
        
        # Dapatkan kode untuk huruf hasil pergeseran
        shifted_char = huruf_list[new_index]
        cipher_code = huruf_to_kode[shifted_char]
        
        ciphertext_codes.append(cipher_code)
    
    return " ".join(ciphertext_codes)

# Fungsi untuk dekripsi
def decrypt_four_square_cipher(ciphertext, key):
    """
    Implementasi dekripsi untuk modifikasi Four Square Cipher
    """
    # Pisahkan ciphertext menjadi kode-kode
    cipher_codes = ciphertext.strip().split()
    
    # Validasi key
    key_str = str(key).replace(" ", "")
    if not all(c.isdigit() for c in key_str):
        st.error("Error: Key hanya boleh berisi angka")
        return ""
    
    if len(key_str) > 5:
        st.error("Error: Key maksimal 5 angka")
        return ""
    
    # Konversi key ke list angka
    key_digits = [int(d) for d in key_str]
    
    # Inisialisasi plaintext
    plaintext_chars = []
    
    # Proses dekripsi per kode
    for i, code in enumerate(cipher_codes):
        # Dapatkan key digit untuk kode ini
        key_digit = key_digits[i % len(key_digits)]
        
        # Validasi kode
        if code not in kode_to_huruf:
            st.error(f"Error: Kode '{code}' tidak valid")
            return ""
        
        # Dapatkan huruf dari kode
        shifted_char = kode_to_huruf[code]
        
        # Dapatkan indeks huruf
        shifted_index = huruf_list.index(shifted_char)
        
        # Hitung indeks asli (mundur sesuai key)
        original_index = (shifted_index - key_digit) % len(huruf_list)
        
        # Dapatkan huruf asli
        original_char = huruf_list[original_index]
        
        plaintext_chars.append(original_char)
    
    return " ".join(plaintext_chars)

# Interface utama
st.markdown("---")
st.subheader("🔐 ENKRIPSI & DEKRIPSI")

# Pilih mode
mode = st.radio("Pilih Mode:", ["Enkripsi", "Dekripsi"], horizontal=True)

# Input berdasarkan mode
if mode == "Enkripsi":
    col_input1, col_input2 = st.columns(2)
    
    with col_input1:
        plaintext = st.text_input("Masukkan Plaintext:", "FADINA", help="Masukkan teks yang akan dienkripsi (huruf A-Z)")
    
    with col_input2:
        key = st.text_input("Masukkan Key:", "23547", help="Masukkan key (angka, maksimal 5 digit)")
    
    if st.button("🚀 Enkripsi", type="primary"):
        if plaintext and key:
            with st.spinner("Melakukan enkripsi..."):
                ciphertext = encrypt_four_square_cipher(plaintext, key)
                if ciphertext:
                    st.success("Enkripsi Berhasil!")
                    
                    # Tampilkan hasil dalam box
                    st.info(f"**Plaintext:** {plaintext}")
                    st.info(f"**Key:** {key}")
                    st.info(f"**Ciphertext:** {ciphertext}")
                    
                    # Tampilkan detail proses
                    with st.expander("📖 Lihat Detail Proses"):
                        st.write("**Proses Enkripsi:**")
                        plaintext_clean = plaintext.upper().replace(" ", "")
                        key_str = str(key).replace(" ", "")
                        key_digits = [int(d) for d in key_str]
                        
                        process_data = []
                        for i, char in enumerate(plaintext_clean):
                            key_digit = key_digits[i % len(key_digits)]
                            char_index = huruf_list.index(char)
                            new_index = (char_index + key_digit) % len(huruf_list)
                            shifted_char = huruf_list[new_index]
                            cipher_code = huruf_to_kode[shifted_char]
                            
                            process_data.append({
                                "Huruf": char,
                                "Key Digit": key_digit,
                                "Indeks Awal": char_index,
                                "Indeks Baru": new_index,
                                "Huruf Baru": shifted_char,
                                "Kode": cipher_code
                            })
                        
                        st.table(pd.DataFrame(process_data))

else:  # Dekripsi
    col_input1, col_input2 = st.columns(2)
    
    with col_input1:
        ciphertext = st.text_input("Masukkan Ciphertext:", "nm blc fnc kc 7 giz", help="Masukkan kode ciphertext yang dipisahkan spasi")
    
    with col_input2:
        key = st.text_input("Masukkan Key:", "23547", help="Masukkan key (angka, maksimal 5 digit)")
    
    if st.button("🔓 Dekripsi", type="primary"):
        if ciphertext and key:
            with st.spinner("Melakukan dekripsi..."):
                plaintext = decrypt_four_square_cipher(ciphertext, key)
                if plaintext:
                    st.success("Dekripsi Berhasil!")
                    
                    # Tampilkan hasil dalam box
                    st.info(f"**Ciphertext:** {ciphertext}")
                    st.info(f"**Key:** {key}")
                    st.info(f"**Plaintext:** {plaintext}")
                    
                    # Tampilkan detail proses
                    with st.expander("📖 Lihat Detail Proses"):
                        st.write("**Proses Dekripsi:**")
                        cipher_codes = ciphertext.strip().split()
                        key_str = str(key).replace(" ", "")
                        key_digits = [int(d) for d in key_str]
                        
                        process_data = []
                        for i, code in enumerate(cipher_codes):
                            if code in kode_to_huruf:
                                key_digit = key_digits[i % len(key_digits)]
                                shifted_char = kode_to_huruf[code]
                                shifted_index = huruf_list.index(shifted_char)
                                original_index = (shifted_index - key_digit) % len(huruf_list)
                                original_char = huruf_list[original_index]
                                
                                process_data.append({
                                    "Kode": code,
                                    "Key Digit": key_digit,
                                    "Huruf Terenkripsi": shifted_char,
                                    "Indeks Terenkripsi": shifted_index,
                                    "Indeks Asli": original_index,
                                    "Huruf Asli": original_char
                                })
                        
                        if process_data:
                            st.table(pd.DataFrame(process_data))

st.markdown("---")

# Contoh penggunaan
st.subheader("📚 CONTOH SOAL")
st.markdown("""
Berikut contoh enkripsi dari dokumen:

**Plaintext:** F A D I N A  
**Key:** 2 3 5 4 7  
**Ciphertext:** nm blc fnc kc 7 giz

*Catatan: Pada contoh di dokumen, terdapat angka '7' dalam ciphertext yang tampaknya merupakan kesalahan penulisan karena seharusnya berupa kode dari tabel alphabet.*
""")

# Informasi tambahan
st.markdown("---")
st.subheader("💡 PEMBAHASAN")
st.markdown("""
Algoritma yang digunakan adalah modifikasi dari **Four Square Cipher** dengan perubahan sebagai berikut:
1. Tabel alphabet dimodifikasi menggunakan kode warna ikan cupang
2. Struktur diubah menjadi enam segitiga (bentuk khusus)
3. Proses enkripsi menggunakan pergeseran dengan pola tertentu

Dengan pendekatan ini, keamanan pesan dapat ditingkatkan melalui kompleksitas pola warna ikan cupang yang unik dan sulit diprediksi.
""")

# Tampilkan tabel tambahan seperti di contoh
st.subheader("📋 TABEL REFERENSI TAMBAHAN")
additional_table_data = [
    ["avt", "ki", "giz", "blc", "wp", "ylo", "rd", "b", "vol", "8", "9", "0"],
         ["gor", "mc", "fcp", "sr", "oa", "y", "pnd", "kg", "kc", "1", "6", "7"],
          ["cl", "bgl", "mrl", "hlb", "nm", "fnc", "nc", "Cpr", "2", "3", "4", "5"]
]

# Tampilkan sebagai tabel sederhana
for row in additional_table_data:
    st.write(" | ".join([str(item) for item in row if item]))

st.markdown("---")
st.success("**TERIMA KASIH** - Sistem kriptografi berbasis pola warna ikan cupang")

# Instruksi penggunaan
with st.expander("ℹ️ Cara Menggunakan Aplikasi"):
    st.markdown("""
    1. **Untuk Enkripsi:**
       - Pilih mode "Enkripsi"
       - Masukkan plaintext (huruf A-Z tanpa spasi)
       - Masukkan key (angka, maksimal 5 digit)
       - Klik tombol "Enkripsi"
    
    2. **Untuk Dekripsi:**
       - Pilih mode "Dekripsi"
       - Masukkan ciphertext (kode dipisahkan spasi)
       - Masukkan key yang sama dengan saat enkripsi
       - Klik tombol "Dekripsi"
    
    3. **Perhatikan:**
       - Key harus sama antara enkripsi dan dekripsi
       - Plaintext hanya menerima huruf A-Z
       - Key hanya menerima angka 0-9
    """)

# Catatan kaki
st.caption("Dikembangkan oleh Gilang Yudha Prajatma - Modifikasi Kriptografi Berbasis Pola Warna Ikan Cupang")
