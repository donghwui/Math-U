import random
import json
import pickle
import numpy as np

# Lemmatization Library
import nltk
nltk.download ('punkt')
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer = WordNetLemmatizer

#reads the intents.json file and passes over to the dictionary
intents = json.loads(open('intents.json').read())

words=[]
classes=[]
documents=[]

#ignores punctuation
ignore_letters = ['?', '!', '.', ',']

for intent in intents['intents']:
  for pattern in intent['patterns']:
    #tokenizes / splits into words
    word_list = nltk.word_tokenize(pattern)
    words.append(word_list)
    documents.append((word_list), intent['tag'])

print(documents)
