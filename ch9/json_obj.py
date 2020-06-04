import spacy
nlp = spacy.load('en')
doc = nlp(u'I want a Greek pizza.')
orderdict ={}
for token in doc:
  if token.dep_ == 'dobj':
    dobj = token
    orderdict.update(product = dobj.lemma_)
    for child in dobj.lefts:
      if child.dep_ == 'amod' or child.dep_ == 'compound':
        orderdict.update(ptype = child.text )
      elif child.dep_ == 'det':
        orderdict.update(qty = 1 )
      elif child.dep_ == 'nummod':
        orderdict.update(qty = child.text)
    break
print(orderdict)
