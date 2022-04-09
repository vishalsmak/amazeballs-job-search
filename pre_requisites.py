import os
import nltk

# External dependencies for resume parser module

# Install SpaCy Dependencies
os.system('python -m pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz')
#python3 -m spacy download en_core_web_sm

# Install nltk Dependencies
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
