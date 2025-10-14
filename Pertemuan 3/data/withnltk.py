import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import glob
import re
import os
import sys

# Download NLTK data jika diperlukan
# nltk.download('punkt')
# nltk.download('stopwords')

Stopwords = set(stopwords.words('english'))

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

def finding_all_unique_words_and_freq(words):
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def remove_special_characters(text):
    regex = re.compile('[^a-zA-Z0-9\\s]')
    text_returned = re.sub(regex, '', text)
    return text_returned

def preprocess_text(text):
    """Preprocess text: remove special chars, numbers, tokenize, lowercase, remove stopwords"""
    text = remove_special_characters(text)
    text = re.sub(re.compile('\\d'), '', text)
    words = word_tokenize(text)
    words = [word for word in words if len(word) > 1]
    words = [word.lower() for word in words]
    words = [word for word in words if word not in Stopwords]
    return words

# Build the inverted index
print("Building inverted index from documents...")
all_words = []
dict_global = {}
file_folder = 'data/*'
files_with_index = {}
linked_list_data = {}

# First pass: collect all unique words
idx = 1
for file in glob.glob(file_folder):
    print(f"Processing: {file}")
    fname = file
    file_obj = open(file, "r", encoding='utf-8')
    text = file_obj.read()
    file_obj.close()
    
    words = preprocess_text(text)
    dict_global.update(finding_all_unique_words_and_freq(words))
    files_with_index[idx] = os.path.basename(fname)
    idx += 1

unique_words_all = set(dict_global.keys())

# Initialize linked lists for each word
for word in unique_words_all:
    linked_list_data[word] = SlinkedList()

# Second pass: build inverted index
idx = 1
for file in glob.glob(file_folder):
    file_obj = open(file, "r", encoding='utf-8')
    text = file_obj.read()
    file_obj.close()
    
    words = preprocess_text(text)
    word_freq_in_doc = finding_all_unique_words_and_freq(words)
    
    for word, freq in word_freq_in_doc.items():
        if word in linked_list_data:
            linked_list_data[word].append(idx, freq)
    idx += 1

print(f"\nIndex built successfully! Total unique words: {len(unique_words_all)}")
print(f"Documents indexed: {len(files_with_index)}")

def process_query(query):
    """Process boolean query and return matching documents"""
    query_words = word_tokenize(query)
    
    connecting_words = []
    different_words = []
    
    # Parse query into words and operators
    for word in query_words:
        if word.lower() not in ["and", "or", "not"]:
            different_words.append(word.lower())
        else:
            connecting_words.append(word.lower())
    
    print(f"Search words: {different_words}")
    print(f"Operators: {connecting_words}")
    
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
            print(f"'{word}' found in documents: {[i+1 for i, bit in enumerate(zeroes_and_ones) if bit == 1]}")
        else:
            print(f"'{word}' not found in any document")
            return []
    
    # Process boolean operations
    if not connecting_words:  # Single word query
        result_vector = zeroes_and_ones_of_all_words[0]
    else:
        result_vector = zeroes_and_ones_of_all_words[0]
        op_index = 0
        
        for i in range(len(connecting_words)):
            operator = connecting_words[i]
            next_vector = zeroes_and_ones_of_all_words[i + 1]
            
            if operator == "and":
                result_vector = [w1 & w2 for w1, w2 in zip(result_vector, next_vector)]
            elif operator == "or":
                result_vector = [w1 | w2 for w1, w2 in zip(result_vector, next_vector)]
            elif operator == "not":
                # NOT operation: A AND NOT B
                not_vector = [1 - bit for bit in next_vector]
                result_vector = [w1 & w2 for w1, w2 in zip(result_vector, not_vector)]
    
    # Get matching documents
    matching_files = []
    for i, bit in enumerate(result_vector):
        if bit == 1:
            matching_files.append(files_with_index[i + 1])
    
    return matching_files

def print_document_list():
    """Print list of all documents"""
    print("\nAvailable documents:")
    for idx, filename in files_with_index.items():
        print(f"{idx}. {filename}")

# Main query interface
def main():
    print("\n" + "="*50)
    print("BOOLEAN RETRIEVAL SYSTEM")
    print("="*50)
    print_document_list()
    
    print("\nQuery Examples:")
    print("• badminton")
    print("• badminton AND tennis") 
    print("• modi OR obama")
    print("• baseball NOT tennis")
    print("• queen AND elizabeth")
    print("• quit (to exit)")
    
    while True:
        print("\n" + "-"*30)
        query = input("Enter your query: ").strip()
        
        if query.lower() == 'quit':
            print("Goodbye!")
            break
            
        if not query:
            continue
            
        results = process_query(query)
        
        if results:
            print(f"\nFound {len(results)} matching document(s):")
            for i, filename in enumerate(results, 1):
                print(f"{i}. {filename}")
                
            # Show content preview for single result
            if len(results) == 1:
                filename = results[0]
                filepath = os.path.join('data', filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        preview = content[:200] + "..." if len(content) > 200 else content
                        print(f"\nPreview of '{filename}':")
                        print(preview)
                except:
                    print(f"\n(Could not read preview of {filename})")
        else:
            print("\nNo documents found matching your query.")

if __name__ == "__main__":
    main()