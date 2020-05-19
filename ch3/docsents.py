import spacy
nlp = spacy.load('en')
doc = nlp(u'A severe storm hit the beach. It started to rain.')
for sent in doc.sents:
  [sent[i] for i in range(len(sent))]
