import json
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pickle

# Download NLTK
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

def train_model():
    # init the lemmatizer
    lemmatizer = WordNetLemmatizer()

    # load existing intents
    with open('intents.json') as file:
        intents = json.load(file)

    words = []
    classes = []
    documents = []
    ignore_letters = ['?', '!', '.', ',']

    # stop words set
    stop_words = set(stopwords.words('english'))

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            # tokenize
            word_list = nltk.word_tokenize(pattern)
            # normalize (lowercase + remove punctuation)
            word_list = [lemmatizer.lemmatize(word.lower()) for word in word_list if word not in ignore_letters]
            # remove stop words
            word_list = [word for word in word_list if word not in stop_words]
            # append to our collections
            words.extend(word_list)
            documents.append((word_list, intent['tag']))
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    # create training data
    training = []
    output_empty = [0] * len(classes)

    # bag of words for each document
    for doc in documents:
        bag = [0] * len(words)
        pattern_words = doc[0]
        for w in pattern_words:
            for i, word in enumerate(words):
                if word == w:
                    bag[i] = 1

        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        training.append([bag, output_row])

    # shuffle data and convert to array
    random.shuffle(training)
    training = np.array(training)

    # create train and test lists
    train_x = list(training[:, 0])
    train_y = list(training[:, 1])

    # build neural network
    model = Sequential()
    model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(train_y[0]), activation='softmax'))

    # compile model
    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    # fit model
    model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

    # save model
    model.save('chatbot_model.h5')

    # save label encoder
    with open('label_encoder.pkl', 'wb') as file:
        pickle.dump(classes, file)

train_model()
