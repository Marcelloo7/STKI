# ===========================================
# Eksperimen: Sistem Akademik Berbasis OOP
# Materi: Class, Object, Inheritance, Encapsulation, Polymorphism
# ===========================================

# 1️⃣ Membuat kelas dasar
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.__ipk = 0.0  # atribut private

    def set_ipk(self, nilai):
        if 0.0 <= nilai <= 4.0:
            self.__ipk = nilai
        else:
            print("Nilai IPK tidak valid!")

    def get_ipk(self):
        return self.__ipk

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}, IPK: {self.__ipk}")

# 2️⃣ Pewarisan (Inheritance)
class MahasiswaAktif(Mahasiswa):
    def __init__(self, nama, nim, jurusan, semester):
        super().__init__(nama, nim, jurusan)
        self.semester = semester
        self.krs = []

    def tambah_matkul(self, matkul):
        self.krs.append(matkul)

    # Polymorphism (override method)
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Semester: {self.semester}, Mata Kuliah: {', '.join(self.krs) if self.krs else 'Belum ada'}")

# 3️⃣ Class lain yang berdiri sendiri
class Dosen:
    def __init__(self, nama, nidn, bidang):
        self.nama = nama
        self.nidn = nidn
        self.bidang = bidang

    def tampilkan_info(self):
        print(f"Dosen: {self.nama}, NIDN: {self.nidn}, Bidang: {self.bidang}")

# 4️⃣ Demonstrasi penggunaan OOP
mhs1 = Mahasiswa("Andi", "A001", "Informatika")
mhs1.set_ipk(3.75)
mhs1.tampilkan_info()

print("\n--- Mahasiswa Aktif ---")
mhs2 = MahasiswaAktif("Budi", "A002", "Sistem Informasi", 5)
mhs2.set_ipk(3.2)
mhs2.tambah_matkul("Pemrograman Python")
mhs2.tambah_matkul("Basis Data")
mhs2.tampilkan_info()

print("\n--- Dosen ---")
dsn1 = Dosen("Dr. Siti", "D123", "Kecerdasan Buatan")
dsn1.tampilkan_info()
