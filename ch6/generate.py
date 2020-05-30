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
def pron_pattern(doc):
  plural = ['we','us','they','them']
  for token in doc:
    if token.dep_ == 'dobj' and token.tag_ == 'PRP':
      if token.text in plural:
        return 'plural'
      else:
        return 'singular'
  return 'not found'
def find_noun(sents, num):
  if num == 'plural':
    taglist = ['NNS','NNPS']
  if num == 'singular':
    taglist = ['NN','NNP']
  for sent in reversed(sents):
    for token in sent:
      if token.tag_ in taglist:
        return token.text
  return 'Noun not found'
def gen_utterance(doc, noun):
  sent = ''
  for i,token in enumerate(doc):
    if token.dep_ == 'dobj' and token.tag_ == 'PRP':
      sent = doc[:i].text + ' ' + noun + ' ' + doc[i+1:len(doc)-2].text + 'too.'
      return sent
  return 'Failed to generate an utterance' 
doc = nlp(u'The symbols are clearly distinguishable. I can recognize them promptly.')
sents = list(doc.sents)
response = ''
noun = ''
for i, sent in enumerate(sents):
  if dep_pattern(sent) and pos_pattern(sent):
    noun = find_noun(sents[:i], pron_pattern(sent))
    if noun != 'Noun not found':
      response = gen_utterance(sents[i],noun)
      break
print(response)
