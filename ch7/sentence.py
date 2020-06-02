import spacy
nlp = spacy.load('en')
doc = nlp(u"I have a relaxed pair of jeans. Now I want a skinny pair.")
spans = list(doc.sents)
from spacy import displacy
displacy.serve(spans, style='dep')
