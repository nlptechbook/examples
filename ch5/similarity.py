import spacy
nlp = spacy.load('en')
doc=nlp('I want a green apple.')
doc.similarity(doc[2:5])
