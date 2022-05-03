import string

import nltk

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
    #lemantize
    
    lemen =[]
    
    for word in words:
        tmp = wordnet.synsets(word)[0].pos()
        if (tmp == 'v'):
            word = WordNetLemmatizer().lemmatize(word,'v')
        if (tmp == 'a'):
            word = WordNetLemmatizer().lemmatize(word,'a')
        if (tmp == 'n'):
            word = WordNetLemmatizer().lemmatize(word,'n')
        else:
            word = WordNetLemmatizer().lemmatize(word)
        lemen.append (word)
    # stem words
    #porter = PorterStemmer()
    #stemmed = [porter.stem(word) for word in words]
    return lemen

txt = "hello I AM YOUR Horrible nightmare, YOU ARE AFRAID OF a goose I gave you geese!! @# HE HE HE HE"
print(normalizeText(txt))