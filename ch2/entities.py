import spacy
nlp = spacy.load('en')
doc = nlp(u'I have flown to LA. Now I am flying to Frisco.')
for token in doc:
  if token.ent_type != 0:
    print(token.text, token.ent_type_)
