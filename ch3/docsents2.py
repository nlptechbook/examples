import spacy
nlp = spacy.load('en')
doc = nlp(u'A severe storm hit the beach. It started to rain.')
for i,sent in enumerate(doc.sents):
  if i==1 and sent[0].pos_== 'PRON':
    print('The second sentence begins with a pronoun.')
