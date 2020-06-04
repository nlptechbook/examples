import spacy
nlp = spacy.load('en')
#apply the pipeline to the sample sentence
doc = nlp(u'I want to place an order for a pizza.')
# extract the direct object and its transitive verb
dobj = ''
tverb = ''
for token in doc:
  if token.dep_ == 'dobj':
    dobj = token
    tverb = token.head
# extract the verb for the intent's definition
intentVerb = ''
verbList = ['want', 'like', 'need', 'order']
if tverb.text in verbList:
  intentVerb = tverb
else:
  if tverb.head.dep_ == 'ROOT':
    intentVerb = tverb.head
# extract the object for the intent's definition
intentObj = ''
objList = ['pizza', 'cola']
if dobj.text in objList:
  intentObj = dobj
else:
  for child in dobj.children:
    if child.dep_ == 'prep':
      intentObj = list(child.children)[0]
      break
    elif child.dep_ == 'compound':
      intentObj = child
      break
# print the intent expressed in the sample sentence
print(intentVerb.text + intentObj.text.capitalize())
