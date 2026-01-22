import numpy as np
from sklearn.metrics import precision_score, recall_score, accuracy_score
from sklearn.cluster import KMeans

# =========================================================
# PART 1: SPAM DETECTION EVALUATION
# =========================================================
print("=== PART 1: SPAM DETECTION EVALUATION ===")

# 1 = spam, 0 = non-spam
# Ground truth (100 spam, 900 non-spam)
y_true = np.array([1]*100 + [0]*900)

# Sistem mendeteksi 110 spam
# Dari 110: 90 benar spam, 20 salah (false positive)
y_pred = np.array([1]*90 + [0]*10 + [1]*20 + [0]*880)

precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
accuracy = accuracy_score(y_true, y_pred)

print(f"Precision : {precision:.2f}")
print(f"Recall    : {recall:.2f}")
print(f"Accuracy  : {accuracy:.2f}")

# =========================================================
# PART 2: BIAS CASE (PRECISION TINGGI, RECALL RENDAH)
# =========================================================
print("\n=== PART 2: BIAS CASE ===")

# Sistem hanya mendeteksi 1 spam dan itu benar
y_pred_bias = np.array([1] + [0]*999)

precision_bias = precision_score(y_true, y_pred_bias)
recall_bias = recall_score(y_true, y_pred_bias)
accuracy_bias = accuracy_score(y_true, y_pred_bias)

print(f"Precision : {precision_bias:.2f}")
print(f"Recall    : {recall_bias:.2f}")
print(f"Accuracy  : {accuracy_bias:.2f}")

print("\nKesimpulan: Precision dan Accuracy tinggi TIDAK menjamin sistem bagus jika Recall rendah.")

# =========================================================
# PART 3: WEB USAGE MINING (CLICKSTREAM ANALYSIS)
# =========================================================
print("\n=== PART 3: WEB USAGE MINING ===")

"""
Fitur:
- jumlah_halaman_dikunjungi
- durasi_kunjungan (menit)
- jumlah_klik
"""

# Data simulasi perilaku pengguna
X = np.array([
    [5, 2, 10],    # user cepat
    [50, 30, 200], # user aktif
    [10, 5, 20],
    [60, 45, 300],
    [3, 1, 5],
    [55, 40, 250],
])

kmeans = KMeans(n_clusters=2, random_state=42)
labels = kmeans.fit_predict(X)

print("Cluster Pengguna:")
for i, label in enumerate(labels):
    print(f"User {i+1} -> Cluster {label}")

print("\nInterpretasi:")
print("Cluster 0 : Pengguna pasif")
print("Cluster 1 : Pengguna aktif")

# =========================================================
# PART 4: KESIMPULAN EKSPERIMEN
# =========================================================
print("\n=== KESIMPULAN ===")
print("""
1. Precision mengukur ketepatan hasil deteksi.
2. Recall mengukur kemampuan menemukan semua spam.
3. Accuracy bisa menyesatkan jika data tidak seimbang.
4. Web Usage Mining membantu memahami perilaku pengguna.
5. Clustering clickstream bisa dipakai untuk:
   - targeting iklan
   - rekomendasi konten
   - optimasi website
""")
