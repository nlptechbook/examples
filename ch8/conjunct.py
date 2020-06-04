import spacy
nlp = spacy.load('en')
doc = nlp(u'I want a pizza and cola.')
#extract the direct object and the conjunct associated with it
for token in doc:
  if token.dep_ == 'dobj':
    dobj = [token.text]
    conj = [t.text for t in token.conjuncts]
#compose the list of the extracted elements
dobj_conj = dobj + conj
print(dobj_conj)
