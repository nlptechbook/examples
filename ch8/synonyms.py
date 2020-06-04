import spacy
nlp = spacy.load('en')
doc = nlp(u'I want a dish.')
#extract the transitive verb and its direct object from the dependency tree
for token in doc:
  if token.dep_ == 'dobj':
    verb = token.head.text
    dobj = token.text
#create a list of tuples for possible verb synonyms
verbList = [('order','want','give','make'),('show','find')]
#find the tuple containing the transitive verb extracted from the sample
verbSyns = [item for item in verbList if verb in item]
#create a list of tuples for possible direct object synonyms
dobjList = [('pizza','pie','dish'),('cola','soda')]
#find the tuple containing the direct object extracted from the sample
dobjSyns = [item for item in dobjList if dobj in item]
#replace the transitive verb and the direct object with synonyms supported by the application
#and compose the string that represents the intent
intent = verbSyns[0][0] + dobjSyns[0][0].capitalize()
print(intent)
