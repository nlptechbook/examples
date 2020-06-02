import spacy
nlp = spacy.load('en')
def det_destination(doc):
  for i, token in enumerate(doc):
    if token.ent_type != 0 and token.ent_type_ == 'GPE':
      while True:
        token = token.head
        if token.text == 'to':
          return doc[i].text
        if token.head == token:
          return 'Failed to determine'
  return 'Failed to determine'
def guess_destination(doc):
  for token in doc:
    if token.ent_type != 0 and token.ent_type_ == 'GPE':
      return token.text
  return 'Failed to determine' 
def gen_response(doc):
  dest = det_destination(doc)
  if dest != 'Failed to determine':
    return 'When do you need to be in ' + dest + '?'
  dest = guess_destination(doc)
  if dest != 'Failed to determine':
    return 'You want a ticket to ' + dest +', right?'
  return 'Are you flying somewhere?'
doc = nlp(u'I am going to the conference in Berlin.')
print(gen_response(doc))
