import spacy
nlp = spacy.load('en')
doc = nlp(u'show me the best hotel in berlin')
for token in doc:
  if token.dep_ == 'dobj':
    print(token.head.text + token.text.capitalize())
