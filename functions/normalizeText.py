import string

import nltk

nltk.download("punkt")
nltk.download("wordnet")
nltk.download("stopwords")

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
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
    # lemantize
    lemen = []
    for word in words:
        try:
            tmp = wordnet.synsets(word)[0].pos()
            if tmp == "v":
                word = WordNetLemmatizer().lemmatize(word, "v")
            if tmp == "a":
                word = WordNetLemmatizer().lemmatize(word, "a")
            if tmp == "n":
                word = WordNetLemmatizer().lemmatize(word, "n")
            if tmp == "r":
                word = WordNetLemmatizer().lemmatize(word, "r")

            lemen.append(word)
        except:
            lemen.append(word)
    # stem words
    return lemen
