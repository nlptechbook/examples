import spacy
nlp = spacy.load('en')
doc = nlp(u'A noun chunk is a phrase that has a noun as its head.')
for chunk in doc.noun_chunks:
  print(chunk)
