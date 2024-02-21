import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from collections import Counter
import string

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Read the text file
with open('insert_filename_here', 'r', encoding='utf-8') as f:
    text = f.read()

# Tokenize the text into words
tokens = word_tokenize(text)

# Initialize Porter Stemmer
stemmer = PorterStemmer()

# Remove non-alphanumeric characters and convert words to lowercase
# Only include words longer than 2 characters
words = [word.lower() for word in tokens if word.isalnum() and len(word) >= 3]

# Additional stopwords
custom_stopwords = set(['insert', 'custom', 'stopwords', 'here'])

# Combine NLTK stopwords with custom stopwords
stop_words = set(stopwords.words('english')) | custom_stopwords

# Remove stopwords
filtered_words = [word for word in words if word not in stop_words]

# Perform stemming
stemmed_words = [stemmer.stem(word) for word in filtered_words]

# Count the frequency of each word (with stemming)
#word_freq = Counter(stemmed_words)

# Count the frequency of each word (without stemming)
word_freq = Counter(filtered_words)

# Sort the word frequencies in descending order
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# Write the sorted word frequencies to a text file
with open('word_frequencies.txt', 'w', encoding='utf-8') as output_file:
    for word, freq in sorted_word_freq:
        output_file.write(f'{freq}: {word}\n')
