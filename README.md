# AI-CHATBOT-WITH-NLP

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: DINESH

*INTERN ID*: CT04DH1263

*DOMAIN*: PYTHON

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

# TASK DESCRIPTION

In this project, I developed a basic chatbot using Natural Language Processing (NLP) techniques with the help of Python libraries like NLTK (Natural Language Toolkit) and Scikit-learn. The main objective of the chatbot was to respond to user queries in natural language, simulating a basic conversational experience. The chatbot was designed to read from a text-based knowledge source and return the most relevant response to a user's question.

The first step was setting up the Python environment and installing the required libraries. I used Python 3.13 along with packages like nltk for natural language processing, and scikit-learn for text vectorization and similarity calculation. The corpus for the chatbot was stored in a text file (knowledge.txt) that contained predefined information about various topics such as programming languages, artificial intelligence, and general knowledge concepts.

I used nltk to tokenize the text data into sentences and words. Tokenization is essential to break down the input text into manageable pieces. Additionally, I implemented lemmatization to reduce words to their root forms, which helps improve the matching accuracy when comparing user inputs with the stored knowledge. For example, the words "running", "ran", and "runs" are all reduced to their base form "run", allowing the chatbot to better understand the meaning regardless of the verb tense or form.

To find the best possible match for user queries, I used the TfidfVectorizer from the scikit-learn library. This method transforms the text data into numerical values based on term frequency and inverse document frequency, helping the chatbot determine the importance of each word in the context. Once the user enters a question, it is compared with the vectorized sentences from the knowledge base using cosine similarity. The sentence with the highest similarity score is then selected and returned as the chatbot’s response.

The chatbot operates in a simple command-line interface (CLI) where the user types questions and receives responses. If the similarity score is too low, the bot replies with a default fallback response like “I’m sorry, I don’t understand that.” The chatbot runs in a continuous loop until the user types a termination keyword like "bye" to end the session.

During implementation, I encountered challenges such as missing NLP data packages like punkt and wordnet, which are essential for tokenization and lemmatization. I resolved these by downloading the necessary NLTK datasets through Python commands. I also handled errors related to library versions and Python path configurations.

This project demonstrates the practical use of Natural Language Processing in building interactive systems. Though basic, the chatbot showcases core NLP concepts such as tokenization, lemmatization, text vectorization, and semantic similarity matching. It can be extended further to include web search integration, voice interface, or even a graphical UI. It is applicable in areas like virtual customer support, FAQ answering systems, educational assistants, and simple information bots. This task helped me understand how computers can be trained to understand and respond to human language, marking a significant step toward intelligent conversational agents.

# OUTPUT

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/54c7bfb9-5468-4b1e-b2e7-107534fd0329" />
