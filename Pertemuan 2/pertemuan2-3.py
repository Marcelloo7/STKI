# ===========================================
# Eksperimen: Pengelolaan Data Mahasiswa
# Materi: Function, Tuple, Dictionary
# ===========================================

# 1️⃣ Fungsi untuk menampilkan data mahasiswa
def tampilkan_data(mahasiswa):
    print("\n=== Daftar Mahasiswa ===")
    for mhs in mahasiswa:
        nama, nim, nilai = mhs  # tuple unpacking
        print(f"{nama} ({nim}) → Nilai: {nilai}")

# 2️⃣ Fungsi untuk menghitung rata-rata nilai
def hitung_rata(mahasiswa):
    total = sum([mhs[2] for mhs in mahasiswa])
    return total / len(mahasiswa)

# 3️⃣ Fungsi untuk mengonversi data tuple menjadi dictionary
def buat_dict(mahasiswa):
    data_dict = {mhs[1]: {"nama": mhs[0], "nilai": mhs[2]} for mhs in mahasiswa}
    return data_dict

# 4️⃣ Data awal (list berisi tuple)
data_mahasiswa = [
    ("Andi", "A001", 85),
    ("Budi", "A002", 72),
    ("Citra", "A003", 90),
    ("Dewi", "A004", 65),
]

# 5️⃣ Menampilkan data menggunakan fungsi
tampilkan_data(data_mahasiswa)

# 6️⃣ Menghitung rata-rata nilai
rata = hitung_rata(data_mahasiswa)
print(f"\nRata-rata nilai kelas: {rata:.2f}")

# 7️⃣ Mengonversi ke dictionary dan menambahkan data baru
data_dict = buat_dict(data_mahasiswa)
data_dict["A005"] = {"nama": "Eko", "nilai": 78}  # update dictionary

# 8️⃣ Menampilkan data dictionary
print("\n=== Data Mahasiswa (Dictionary) ===")
for nim, info in data_dict.items():
    print(f"{info['nama']} ({nim}) → Nilai: {info['nilai']}")

# 9️⃣ Fungsi dengan default parameter dan filtering
def cari_lulus(data, batas=70):
    lulus = {nim: info for nim, info in data.items() if info["nilai"] >= batas}
    return lulus

print("\nMahasiswa yang lulus:")
for nim, info in cari_lulus(data_dict).items():
    print(f"- {info['nama']} ({nim})")

# 🔟 Contoh penggunaan scope variabel
nilai_global = 50

def ubah_nilai(n):
    global nilai_global
    nilai_global += n
    return nilai_global

print("\nNilai global setelah diubah:", ubah_nilai(10))
