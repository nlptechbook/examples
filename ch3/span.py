import spacy
nlp = spacy.load('en')
doc = nlp(u'The Golden Gate Bridge is an iconic landmark in San Francisco.')
[doc[i] for i in range(len(doc))]
span = doc[1:4]
lem_id = doc.vocab.strings[span.text]
span.merge(lemma = lem_id)
