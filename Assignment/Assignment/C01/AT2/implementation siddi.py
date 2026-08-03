# Derivational Morphology and Vocabulary Expansion

# Dictionary containing root words and their derived forms
word_dict = {
    "teach": ["teacher", "teaching", "taught"],
    "develop": ["developer", "development", "developing"],
    "educate": ["education", "educator", "educational"],
    "act": ["action", "active", "activity", "actor"],
    "create": ["creation", "creative", "creator"],
    "happy": ["happiness", "happily"],
    "beauty": ["beautiful", "beautify"],
    "manage": ["manager", "management"],
    "write": ["writer", "writing"],
    "read": ["reader", "reading"]
}

print("===== Derivational Morphology and Vocabulary Expansion =====")

word = input("Enter a root word: ").lower()

if word in word_dict:
    print("\nRoot Word:", word)
    print("Derived Words:")
    for derived in word_dict[word]:
        print("->", derived)
else:
    print("\nWord not found in dictionary.")