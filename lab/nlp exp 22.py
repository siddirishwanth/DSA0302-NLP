import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter text: ")

doc = nlp(text)

nouns = []
pronouns = ["he", "she", "it", "they", "him", "her", "them"]

for token in doc:
    if token.pos_ in ["PROPN", "NOUN"]:
        nouns.append(token.text)

print("\nReference Resolution:")

for token in doc:
    if token.text.lower() in pronouns:
        if nouns:
            print(token.text, "->", nouns[-1])
