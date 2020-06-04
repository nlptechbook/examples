import spacy
from spacy.pipeline import EntityRecognizer
nlp = spacy.load('en', disable=['ner'])
ner = EntityRecognizer(nlp.vocab)
ner.from_disk('/usr/to/ner')
nlp.add_pipe(ner, "custom_ner")
print(nlp.meta['pipeline'])
doc = nlp(u'Could you pick me up at Solnce?')
for ent in doc.ents:
  print(ent.text, ent.label_)
