import spacy
nlp = spacy.load('en')
doc = nlp(u'I have finished my pizza. I want another one.')
verbList = [('order','want','give','make'),('show','find')]
dobjList = [('pizza','pie','pizzaz'),('cola','soda')]
substitutes = ('one','it','same','more')
intent = {'verb': '', 'dobj': ''}
for sent in doc.sents:
  for token in sent:
    if token.dep_ == 'dobj':
      verbSyns = [item for item in verbList if token.head.text in item]
      dobjSyns = [item for item in dobjList if token.text in item]
      substitute = [item for item in substitutes if token.text in item]
      if (dobjSyns != [] or substitute != []) and verbSyns != []:
        intent['verb'] = verbSyns[0][0]
      if dobjSyns != []:
        intent['dobj'] = dobjSyns[0][0]
intentStr = intent['verb'] + intent['dobj'].capitalize()
print(intentStr)
