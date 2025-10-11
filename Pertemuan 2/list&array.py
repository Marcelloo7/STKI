# ========================================
# Eksperimen: Analisis Nilai Mahasiswa
# ========================================

# 1️⃣ Input nilai (menggunakan list)
nilai = [78, 85, 62, 90, 55, 88, 73]

# 2️⃣ Operator Aritmatika & Relasional
rata_rata = sum(nilai) / len(nilai)
print(f"Nilai rata-rata: {rata_rata:.2f}")

# 3️⃣ Struktur if-elif-else
if rata_rata >= 85:
    kategori = "A (Sangat Baik)"
elif rata_rata >= 70:
    kategori = "B (Baik)"
elif rata_rata >= 60:
    kategori = "C (Cukup)"
else:
    kategori = "D (Kurang)"
print("Kategori kelas:", kategori)

# 4️⃣ Loop for + Statement loncat
print("\nDaftar nilai kelulusan:")
for n in nilai:
    if n < 60:
        continue  # lewati nilai tidak lulus
    print(f"- {n} (Lulus)")

# 5️⃣ While loop
print("\nProses kenaikan nilai hingga di atas rata-rata:")
i = 0
while i < len(nilai):
    if nilai[i] < rata_rata:
        nilai[i] += 5
    i += 1
print("Nilai setelah kenaikan:", nilai)

# 6️⃣ Operasi logika & bitwise
x, y = 5, 3
print("\nOperasi Logika dan Bitwise:")
print(f"x > 2 and y < 5 → {x > 2 and y < 5}")
print(f"x & y (bitwise AND) = {x & y}")

# 7️⃣ List processing (mutable)
nilai.append(100)
nilai.sort(reverse=True)
print("\nNilai akhir (descending):", nilai)
