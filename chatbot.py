import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import string

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Read external file
with open("knowledge.txt", "r", encoding="utf8") as file:
    corpus = file.read()

sent_tokens = nltk.sent_tokenize(corpus)
lemmatizer = WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmatizer.lemmatize(token.lower()) for token in tokens if token not in string.punctuation]

def tokenize(text):
    return LemTokens(nltk.word_tokenize(text))

def response(user_input):
    sent_tokens.append(user_input)
    vectorizer = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfidf = vectorizer.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    score = flat[-2]
    sent_tokens.pop()

    if score == 0:
        return "I'm sorry! I don't understand that."
    else:
        return sent_tokens[idx]

print("ChatBot: Hi! I'm your assistant. Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input == 'bye':
        print("ChatBot: Bye! Have a great day!")
        break
    else:
        print("ChatBot:", response(user_input))
