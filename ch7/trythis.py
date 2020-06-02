import spacy
nlp = spacy.load('en')
doc = nlp(u"I want a Greek pizza.")
from spacy import displacy
options = {'compact': True, 'font': 'Tahoma','collapse_phrases':True}
displacy.serve(doc, style='dep', options=options)
