import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download required resources (runs once)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)

sample_text = """Artificial Intelligence is rapidly transforming modern industries. 
Engineers are building systems that can learn, reason, and adapt autonomously. 
Does this technology simplify our daily challenges?"""

# 1. Sentence Tokenization
sentences = sent_tokenize(sample_text)
print("--- 1. Sentence Tokenization ---")
for idx, s in enumerate(sentences, 1):
    print(f"[{idx}] {s}")

# 2. Word Tokenization
words = word_tokenize(sample_text)
print("\n--- 2. Word Tokenization (First 15 Words) ---")
print(words[:15])

# 3. Stopwords Filtering
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in words if w.isalnum() and w.lower() not in stop_words]
print("\n--- 3. Stopwords Filtering (Sample) ---")
print(filtered_words[:12])

# 4. Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(w) for w in filtered_words]
print("\n--- 4. Porter Stemming ---")
for orig, stem in list(zip(filtered_words, stemmed_words))[:8]:
    print(f"{orig:<15} -> {stem}")

# 5. POS Tagging
pos_tags = nltk.pos_tag(word_tokenize(sentences[0]))
print("\n--- 5. Part-of-Speech (POS) Tagging (Sentence 1) ---")
for word, tag in pos_tags:
    print(f"{word:<15} : {tag}")

print("\nPrasanna Pokharel")
print("Rollno: 24")
print("LAB IV-5")