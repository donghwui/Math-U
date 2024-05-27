import json
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Load existing intents
with open('intents.json') as file:
    intents = json.load(file)

# Assume new_intents is fetched from the scraping function
# Merge new patterns into existing intents
for new_intent in new_intents['intents']:
    for intent in intents['intents']:
        if intent['tag'] == new_intent['tag']:
            intent['patterns'].extend(new_intent['patterns'])
            break
    else:
        # If no existing tag matches, add as a new intent
        intents['intents'].append(new_intent)

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

# Stop words set
stop_words = set(stopwords.words('english'))

for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize
        word_list = nltk.word_tokenize(pattern)
        # Normalize (lowercase + remove punctuation)
        word_list = [lemmatizer.lemmatize(word.lower()) for word in word_list if word not in ignore_letters]
        # Remove stop words
        word_list = [word for word in word_list if word not in stop_words]
        # POS tagging (optional here, just for demo)
        pos_tags = pos_toTag(word_list)
        # Append to our collections
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

print("Sample document:", documents[0])
