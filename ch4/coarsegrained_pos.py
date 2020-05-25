import spacy
nlp = spacy.load('en')
doc = nlp(u"The firm earned $1.5 million in 2017.")
for token in doc:
  print(token.text, token.pos_, spacy.explain(token.pos_))
