import string

import nltk

nltk.download()

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

def normalizeText(text):

    tokens = word_tokenize(text)
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove punctuation from each word
    table = str.maketrans("", "", string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    # filter out stop words
    stop_words = set(stopwords.words("english"))
    words = [w for w in words if not w in stop_words]
    #lemantize
    lematizer = WordNetLemmatizer()
    lem = [lematizer.lemmatize(word) for word in words]
    # stem words
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in lem]
    return stemmed
