# ========================================
# Eksperimen Minggu 4 - Text Preprocessing
# ========================================

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# ----------------------------------------
# 1️⃣ Unduh resource NLTK (pertama kali saja)
# ----------------------------------------
nltk.download('punkt')
nltk.download('stopwords')

# ----------------------------------------
# 2️⃣ Baca teks mentah dari file
# ----------------------------------------
with open("contoh_teks.txt", "r", encoding="utf-8") as f:
    teks_mentah = f.read()

print("=== TEKS MENTAH ===")
print(teks_mentah)
print()

# ----------------------------------------
# 3️⃣ Case Folding (ubah jadi huruf kecil)
# ----------------------------------------
teks_lower = teks_mentah.lower()
print("=== SETELAH CASE FOLDING ===")
print(teks_lower)
print()

# ----------------------------------------
# 4️⃣ Tokenizing (pecah jadi kata)
# ----------------------------------------
tokens = word_tokenize(teks_lower)
print("=== HASIL TOKENIZING ===")
print(tokens)
print()

# ----------------------------------------
# 5️⃣ Stopword Removal
# ----------------------------------------
stop_words = set(stopwords.words('indonesian'))
filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

print("=== SETELAH STOPWORD REMOVAL ===")
print(filtered_tokens)
print()

# ----------------------------------------
# 6️⃣ Stemming (ubah ke bentuk dasar)
# ----------------------------------------
factory = StemmerFactory()
stemmer = factory.create_stemmer()

hasil_stemming = [stemmer.stem(word) for word in filtered_tokens]
print("=== HASIL STEMMING ===")
print(hasil_stemming)
print()

# ----------------------------------------
# 7️⃣ Simpan hasil ke file output
# ----------------------------------------
with open("output_preprocessing.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(hasil_stemming))

print("✅ Hasil preprocessing disimpan di 'output_preprocessing.txt'")
