import spacy
nlp = spacy.load('en')
doc = nlp(u'this product integrates both libraries for downloading and
applying patches')
for token in doc:
  print(token.text, token.lemma_)
