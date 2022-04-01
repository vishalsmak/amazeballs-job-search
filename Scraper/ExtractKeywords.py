import re
import nltk
from rake_nltk import Rake

stopwords_present = False

class ExtractKeywords:
    
    def extract(self, str):
        global stopwords_present

        if not stopwords_present:
            nltk.download('stopwords')
            nltk.download('punkt')
            stopwords_present = True

        str = str.replace('\n', ' ')
        str = re.sub(' +', ' ', str)
        r = Rake()
        r.extract_keywords_from_text(str)
        return r.get_ranked_phrases()[0:10]
