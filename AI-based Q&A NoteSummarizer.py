import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import defaultdict

# Initialize NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Function to summarize notes
def summarize_notes(notes):
    # Tokenize notes into sentences
    sentences = sent_tokenize(notes)

    # Create a dictionary to store sentence scores
    sentence_scores = defaultdict(int)

    # Calculate sentence scores based on word frequency
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    word_freq = defaultdict(int)
    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        for word in words:
            if word not in stop_words:
                stemmed_word = stemmer.stem(word)
                word_freq[stemmed_word] += 1

    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        for word in words:
            if word not in stop_words:
                stemmed_word = stemmer.stem(word)
                sentence_scores[sentence] += word_freq[stemmed_word]

    # Sort sentences by score and return top-ranked sentences
    ranked_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    return ranked_sentences

# Function to answer questions
def answer_question(notes, question):
    # Tokenize question into words
    question_words = word_tokenize(question.lower())

    # Find relevant sentences in notes
    relevant_sentences = []
    sentences = sent_tokenize(notes)
    for sentence in sentences:
        sentence_words = word_tokenize(sentence.lower())
        for word in question_words:
            if word in sentence_words:
                relevant_sentences.append(sentence)
                break

    # Return top-ranked relevant sentence as answer
    if relevant_sentences:
        return relevant_sentences[0]
    else:
        return "Sorry, no answer found."

# Test the code
notes = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Phasellus sollicitudin condimentum libero, sit amet ultrices augue fringilla eget. 
Nunc et arcu quis orci gravida sodales. 
Fusce ut sem cursus, malesuada sapien non, viverra ex. 
Ut venenatis risus eu mi porta, sed suscipit eros egestas.
"""

question = "What is the main topic of the notes?"
print("Summary:")
ranked_sentences = summarize_notes(notes)
for sentence, score in ranked_sentences[:3]:
    print(sentence)

print("\nAnswer:")
print(answer_question(notes,question))

while True:
    question = input("Ask a question about the notes (or type 'exit' to quit): ")
    if question.lower() == 'stop':
        break
    print("Answer:")
    print(answer_question(notes,question))