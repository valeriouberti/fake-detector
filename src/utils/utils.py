import re
import nltk

# Ensure you have the NLTK punkt tokenizer
nltk.download('punkt')

# Function to clean and preprocess the article text
def preprocess_text(text):
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    return ' '.join(tokens)
