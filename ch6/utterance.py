import spacy
nlp = spacy.load('en')
def dep_pattern(doc):
  for i in range(len(doc)-1):
    if doc[i].dep_ == 'nsubj' and doc[i+1].dep_ == 'aux' and  doc[i+2].dep_ == 'ROOT':
      for tok in doc[i+2].children:
        if tok.dep_ == 'dobj':
          return True
  return False
doc = nlp(u'We can overtake them.')
if dep_pattern(doc):
  print('Found')
else:
  print('Not found')
