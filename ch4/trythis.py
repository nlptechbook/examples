import spacy
nlp = spacy.load('en')
doc = nlp(u"The firm earned $1.5 million in 2017, in comparison with $1.2 million in 2016")
phrase = ''
for token in doc:
  if token.tag_ == '$':
    phrase = token.text
    i = token.i+1
    while doc[i].tag_ == 'CD':
      phrase += doc[i].text + ' '
      i += 1
    phrase = phrase[:-1]
    print(phrase)
