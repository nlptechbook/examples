# For spaCy 2.x
import spacy
from spacy.symbols import ORTH, LEMMA
nlp = spacy.load('en')
doc = nlp(u'I am flying to Frisco')
print([w.text for w in doc])
special_case = [{ORTH: u'Frisco', LEMMA: u'San Francisco'}]
nlp.tokenizer.add_special_case(u'Frisco', special_case)
print([w.lemma_ for w in nlp(u'I am flying to Frisco')])
