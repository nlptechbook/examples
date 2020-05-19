import spacy
nlp = spacy.load('en')
doc = nlp(u'I have flown to LA. Now I am flying to Frisco.')
for sent in doc.sents:
  print([w.text for w in sent if w.dep_ == 'ROOT' or w.dep_ == 'pobj'])
