import spacy
nlp = spacy.load('en')
doc = nlp(u"I can promise it is worth your time.")
sent = ''
for i,token in enumerate(doc):
 if token.tag_ == 'PRP' and doc[i+1].tag_ == 'MD' and doc[i+2].tag_ == 'VB':
   sent = doc[i+1].text.capitalize() + ' ' + doc[i].text
   sent = sent + ' ' + doc[i+2:].text
   break
#By now, you should have: 'Can I promise it is worth your time.'
#Retokenization
doc=nlp(sent)
for i,token in enumerate(doc):
  if token.tag_ == 'PRP' and token.text == 'I':
    sent = doc[:i].text + ' you ' + doc[i+1:].text
    break
#By now, you should have: 'Can you promise it is worth your time.'
doc=nlp(sent)
for i,token in enumerate(doc):
  if token.tag_ == 'PRP$' and token.text == 'your':
    sent = doc[:i].text + ' my ' + doc[i+1:].text
    break
#By now, you should have: 'Can you promise it is worth my time.'
doc=nlp(sent)
for i,token in enumerate(doc):
  if token.tag_ == 'VB':
    sent = doc[:i].text + ' really ' + doc[i:].text
    break
#By now, you should have: 'Can you really promise it is worth my time.'
doc=nlp(sent)
sent = doc[:len(doc)-1].text + '?'
#Finally, you should have: 'Can you really promise it is worth my time?'
print(sent)
