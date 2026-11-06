import nltk

print(f"NLTK version: {nltk.__version__}")

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("omw-1.4")
email_content = (
    "Our team will be working on the upcoming "
    "project deadlines. Please ensure that all "
    "deliverables are submitted before the end "
    "of the week."
)
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()
tokens = word_tokenize(email_content.lower())
stems = [stemmer.stem(token) for token in tokens]

print("\nTASK 2: STEMMING")
print(f"Original Email: {email_content}")
print(f"Stemmed Email: {' '.join(stems)}")
email_content_lemma = (
    "The team members are working on their "
    "tasks diligently. Please ensure that "
    "every report is submitted promptly."
)
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
lemma_tokens = word_tokenize(email_content_lemma.lower())
lemmas = [lemmatizer.lemmatize(token) for token in lemma_tokens]

print("\nTASK 3: LEMMATIZATION")
print(f"Original Email: {email_content_lemma}")
print(f"Lemmatized Email: {' '.join(lemmas)}")
words = ["running", "studies", "working", "children", "connections"]

print("\nTASK 4: COMPARISON")
print(f"{'Original':<15}{'Stemmed':<15}{'Lemmatized (noun)':<20}")

for word in words:
    stemmed = stemmer.stem(word)
    lemmatized = lemmatizer.lemmatize(word)
    print(f"{word:<15}{stemmed:<15}{lemmatized:<20}")

verb_lemma = lemmatizer.lemmatize("running", pos="v")
print(f"\nVerb lemmatization: running -> {verb_lemma}")