# =====================================
# WORD2VEC EXPERIMENT (CBOW & SKIP-GRAM)
# =====================================

from gensim.models import Word2Vec

# =========================
# DATA PREPARATION
# =========================
sentences = [
    "ibu kota negara indonesia adalah jakarta",
    "jakarta adalah ibu kota indonesia",
    "paris adalah ibu kota perancis",
    "perancis memiliki ibu kota paris"
]

# Tokenisasi
tokenized_sentences = [sentence.split() for sentence in sentences]

print("Tokenized Sentences:")
for s in tokenized_sentences:
    print(s)

# =========================
# WORD2VEC - SKIP GRAM
# =========================
print("\n==============================")
print("WORD2VEC - SKIP GRAM")
print("==============================")

skipgram_model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=50,
    window=2,
    min_count=1,
    sg=1,        # Skip-gram
    epochs=100
)

# Vektor kata
print("\nVector 'indonesia':")
print(skipgram_model.wv['indonesia'])

print("\nVector 'jakarta':")
print(skipgram_model.wv['jakarta'])

# Similarity
sim_ij = skipgram_model.wv.similarity('indonesia', 'jakarta')
print("\nSimilarity(indonesia, jakarta):", sim_ij)

# Kata paling mirip
print("\nMost similar to 'jakarta':")
for word, score in skipgram_model.wv.most_similar('jakarta'):
    print(word, ":", score)

# =========================
# WORD2VEC - CBOW
# =========================
print("\n==============================")
print("WORD2VEC - CBOW")
print("==============================")

cbow_model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=50,
    window=2,
    min_count=1,
    sg=0,        # CBOW
    epochs=100
)

print("\nVector 'indonesia':")
print(cbow_model.wv['indonesia'])

print("\nVector 'jakarta':")
print(cbow_model.wv['jakarta'])

# Similarity
sim_ij_cbow = cbow_model.wv.similarity('indonesia', 'jakarta')
print("\nSimilarity(indonesia, jakarta):", sim_ij_cbow)

# Kata paling mirip
print("\nMost similar to 'jakarta':")
for word, score in cbow_model.wv.most_similar('jakarta'):
    print(word, ":", score)

# =========================
# ANALOGY TEST
# =========================
print("\n==============================")
print("ANALOGY TEST")
print("==============================")

try:
    result = skipgram_model.wv.most_similar(
        positive=['jakarta', 'perancis'],
        negative=['indonesia']
    )
    print("jakarta - indonesia + perancis ≈")
    print(result)
except:
    print("Analogy gagal (dataset terlalu kecil)")
