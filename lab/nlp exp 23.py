import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('punkt_tab')

text = input("Enter a paragraph: ")

sentences = sent_tokenize(text)

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(sentences)

scores = []

print("\nSentence Similarity:")

for i in range(len(sentences) - 1):
    score = cosine_similarity(
        vectors[i:i+1],
        vectors[i+1:i+2]
    )[0][0]

    scores.append(score)
    print("Sentence", i + 1, "-> Sentence", i + 2, ":", round(score, 2))

if scores:
    coherence = sum(scores) / len(scores)
else:
    coherence = 1

print("\nCoherence Score:", round(coherence, 2))

if coherence >= 0.3:
    print("Text Status: Coherent")
else:
    print("Text Status: Less Coherent")
