import spacy
nlp = spacy.load('en', disable=['parser'])
doc = nlp(u'I want a green apple.')
for token in doc:
  print(token.text, token.pos_, token.dep_)
