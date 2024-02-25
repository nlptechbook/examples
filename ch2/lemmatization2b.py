# For spaCy 3.x
# See https://github.com/nlptechbook/examples/issues/5
import spacy
from spacy.symbols import LEMMA
nlp = spacy.load('en')
doc = nlp(u'I am flying to Frisco')
print([w.text for w in doc])
nlp.get_pipe("attribute_ruler").add([[{"TEXT": "Frisco"}]], {"LEMMA": "San Francisco"})
print([w.lemma_ for w in nlp(u'I am flying to Frisco')])
