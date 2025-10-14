import glob
import re
import os
import sys

# Stopwords list
Stopwords = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", 
    "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 
    'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 
    'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 
    'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 
    'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 
    'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 
    'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 
    'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 
    'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 
    'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 
    'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 
    'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 
    'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 
    'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', 
    "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', 
    "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', 
    "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', 
    "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"
}

class Node:
    def __init__(self, docId, freq=0):
        self.freq = freq
        self.doc = docId
        self.nextval = None

class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, docId, freq):
        new_node = Node(docId, freq)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.nextval = new_node
            self.tail = new_node

def simple_tokenize(text):
    """Simple tokenizer tanpa NLTK"""
    # Ganti underscore dengan space
    text = text.replace('_', ' ')
    words = text.split()
    # Bersihkan setiap kata dari karakter non-alphabet
    cleaned_words = []
    for word in words:
        cleaned_word = re.sub(r'[^a-zA-Z]', '', word)
        if len(cleaned_word) > 1:  # hanya kata dengan 2 huruf atau lebih
            cleaned_words.append(cleaned_word.lower())
    # Filter stopwords
    cleaned_words = [word for word in cleaned_words if word not in Stopwords]
    return cleaned_words

def finding_all_unique_words_and_freq(words):
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

# Build the inverted index
print("🔨 Building inverted index from documents...")

# Coba beberapa kemungkinan path
possible_paths = [
    'data/*.txt',
    './data/*.txt',
    '../data/*.txt',
    '*.txt',  # Jika file ada di folder yang sama
    'Pertemuan 3/data/*.txt',
    '../Pertemuan 3/data/*.txt'
]

files_with_index = {}
linked_list_data = {}
dict_global = {}

# Cari file yang ada
found_files = []
for path in possible_paths:
    files = glob.glob(path)
    if files:
        found_files.extend(files)
        print(f"✅ Found {len(files)} files with pattern: {path}")

if not found_files:
    print("❌ No files found! Please check:")
    print("   1. File harus berekstensi .txt")
    print("   2. Pastikan folder 'data' ada di lokasi yang benar")
    print("   3. Cek struktur folder:")
    
    # Tampilkan struktur folder saat ini
    print("\n📁 Current directory structure:")
    for root, dirs, files in os.walk('.'):
        level = root.replace('.', '').count(os.sep)
        indent = ' ' * 2 * level
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            if file.endswith('.txt'):
                print(f'{subindent}{file}')
    
    sys.exit(1)

# First pass: collect all unique words
idx = 1
for file_path in found_files:
    print(f"📖 Processing: {os.path.basename(file_path)}")
    try:
        with open(file_path, "r", encoding='utf-8') as file_obj:
            text = file_obj.read()
        
        words = simple_tokenize(text)
        dict_global.update(finding_all_unique_words_and_freq(words))
        files_with_index[idx] = os.path.basename(file_path)
        idx += 1
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")

unique_words_all = set(dict_global.keys())

# Initialize linked lists for each word
for word in unique_words_all:
    linked_list_data[word] = SlinkedList()

# Second pass: build inverted index
idx = 1
for file_path in found_files:
    try:
        with open(file_path, "r", encoding='utf-8') as file_obj:
            text = file_obj.read()
        
        words = simple_tokenize(text)
        word_freq_in_doc = finding_all_unique_words_and_freq(words)
        
        for word, freq in word_freq_in_doc.items():
            if word in linked_list_data:
                linked_list_data[word].append(idx, freq)
        idx += 1
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")

print(f"\n✅ Index built successfully!")
print(f"   Total unique words: {len(unique_words_all)}")
print(f"   Documents indexed: {len(files_with_index)}")

if unique_words_all:
    print(f"   Sample words: {list(unique_words_all)[:10]}...")

def process_query(query):
    """Process boolean query and return matching documents"""
    # Simple tokenizer untuk query
    query_words = query.split()
    
    connecting_words = []
    different_words = []
    
    # Parse query into words and operators
    for word in query_words:
        if word.lower() not in ["and", "or", "not"]:
            different_words.append(word.lower())
        else:
            connecting_words.append(word.lower())
    
    print(f"🔍 Search words: {different_words}")
    if connecting_words:
        print(f"⚡ Operators: {connecting_words}")
    
    total_files = len(files_with_index)
    zeroes_and_ones_of_all_words = []
    
    # Create bit vectors for each search term
    for word in different_words:
        if word in unique_words_all:
            zeroes_and_ones = [0] * total_files
            linkedlist = linked_list_data[word].head
            
            while linkedlist is not None:
                zeroes_and_ones[linkedlist.doc - 1] = 1
                linkedlist = linkedlist.nextval
            
            zeroes_and_ones_of_all_words.append(zeroes_and_ones)
            doc_list = [i+1 for i, bit in enumerate(zeroes_and_ones) if bit == 1]
            print(f"   '{word}' found in documents: {doc_list}")
        else:
            print(f"❌ '{word}' not found in any document")
            return []
    
    # Process boolean operations
    if not connecting_words:  # Single word query
        result_vector = zeroes_and_ones_of_all_words[0]
    else:
        result_vector = zeroes_and_ones_of_all_words[0]
        
        for i in range(len(connecting_words)):
            operator = connecting_words[i]
            next_vector = zeroes_and_ones_of_all_words[i + 1]
            
            if operator == "and":
                result_vector = [w1 & w2 for w1, w2 in zip(result_vector, next_vector)]
                print(f"   Applied AND operation")
            elif operator == "or":
                result_vector = [w1 | w2 for w1, w2 in zip(result_vector, next_vector)]
                print(f"   Applied OR operation")
            elif operator == "not":
                not_vector = [1 - bit for bit in next_vector]
                result_vector = [w1 & w2 for w1, w2 in zip(result_vector, not_vector)]
                print(f"   Applied NOT operation")
    
    # Get matching documents
    matching_files = []
    for i, bit in enumerate(result_vector):
        if bit == 1:
            matching_files.append(files_with_index[i + 1])
    
    return matching_files

def print_document_list():
    """Print list of all documents"""
    print("\n📚 Available documents:")
    for idx, filename in files_with_index.items():
        print(f"   {idx}. {filename}")

# Main query interface
def main():
    print("\n" + "="*60)
    print("🔍 BOOLEAN RETRIEVAL SYSTEM")
    print("="*60)
    print_document_list()
    
    print("\n💡 Query Examples:")
    print("   • badminton")
    print("   • tennis OR badminton") 
    print("   • modi AND india")
    print("   • baseball NOT tennis")
    print("   • queen AND elizabeth")
    print("   • quit (to exit)")
    
    while True:
        print("\n" + "-"*30)
        query = input("Enter your query: ").strip()
        
        if query.lower() == 'quit':
            print("👋 Goodbye!")
            break
            
        if not query:
            continue
            
        results = process_query(query)
        
        if results:
            print(f"\n✅ Found {len(results)} matching document(s):")
            for i, filename in enumerate(results, 1):
                print(f"   {i}. {filename}")
        else:
            print("\n❌ No documents found matching your query.")

if __name__ == "__main__":
    main()