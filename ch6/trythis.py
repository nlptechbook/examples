import spacy
nlp = spacy.load('en')
doc = nlp(u'We can overtake them. You must specify it. I could do it.')
sents = list(doc.sents)
for sent in sents[1:]:
  for i in range(len(sents[0])-1):
    if sents[0][i].dep_ == sent[i].dep_:
      print(sents[0][i].text, sent[i].text, sents[0][i].dep_, spacy.explain(sents[0][i].dep_))
