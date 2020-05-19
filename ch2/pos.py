import spacy
nlp = spacy.load('en')
doc = nlp(u'I have flown to LA. Now I am flying to Frisco.')
print([w.text for w in doc if w.tag_== 'VBG' or w.tag_== 'VB'])
