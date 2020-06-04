def word2int(numword):
  num = 0
  try:
    num = int(numword)
    return num
  except ValueError:
    pass    
  words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight","nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
  for idx, word in enumerate(words):
        if word in numword:
           num = idx 
  return num   
import spacy
nlp = spacy.load('en')
doc = nlp(u'I want twenty two Chicago pizzas.')
orderdict ={}
for token in doc:
  if token.dep_ == 'dobj':
    #print(token.head.text + token.text.capitalize()) 
    dobj = token
    print(list(dobj.lefts))
    orderdict.update(product = dobj.lemma_ )    
    for child in dobj.lefts:
      if child.dep_ == 'amod' or child.dep_ == 'compound': 
        orderdict.update(type = child.text )
      elif child.dep_ == 'det': 
        orderdict.update(qty = 1 )
      elif child.dep_ == 'nummod': 
        orderdict.update(qty = word2int(child.text))
    break
print(orderdict)

