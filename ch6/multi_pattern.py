import spacy
nlp = spacy.load('en')
def dep_pattern(doc):
  for i in range(len(doc)-1):
    if doc[i].dep_ == 'nsubj' and doc[i+1].dep_ == 'aux' and  doc[i+2].dep_ == 'ROOT':
      for tok in doc[i+2].children:
        if tok.dep_ == 'dobj':
          return True
  return False
def pos_pattern(doc):
  for token in doc:
    if token.dep_ == 'nsubj' and token.tag_ != 'PRP':
      return False
    if token.dep_ == 'aux' and token.tag_ != 'MD':
      return False
    if token.dep_ == 'ROOT' and token.tag_ != 'VB':
      return False
    if token.dep_ == 'dobj' and token.tag_ != 'PRP':
      return False
  return True
#Testing code
doc = nlp(u'We can overtake them.')
if dep_pattern(doc) and pos_pattern(doc):
  print('Found')
else:
  print('Not found')
