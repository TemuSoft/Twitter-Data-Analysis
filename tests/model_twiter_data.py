import pandas as pd
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np

np.random.seed(2018)
import nltk

nltk.download("wordnet")
data = pd.read_csv("data/sample.json", error_bad_lines=False)
data_text = data[["columns"]]
data_text["index"] = data_text.index
documents = data_text


def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos="v"))


def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result


doc_sample = documents[documents["index"] == 4310].values[0][0]
print("original document: ")
words = []
for word in doc_sample.split(" "):
    words.append(word)
print(words)
print("\n\n tokenized and lemmatized document: ")
print(preprocess(doc_sample))
