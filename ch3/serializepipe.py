import spacy
nlp = spacy.load('en')
#defining training data
LABEL = 'DISTRICT'
TRAIN_DATA = [
 ('We need to deliver it to Festy.', {
 'entities': [(25, 30, 'DISTRICT')]
  }),
 ('I like red oranges', {
'entities': []
})
]
#performing the training process
ner = nlp.get_pipe('ner')
ner.add_label(LABEL)
nlp.disable_pipes('tagger')
nlp.disable_pipes('parser')
optimizer = nlp.entity.create_optimizer()
import random
for i in range(25):
  random.shuffle(TRAIN_DATA)
  for text, annotations in TRAIN_DATA:
    nlp.update([text], [annotations], sgd=optimizer)
#serializing the pipe to disk
import os
if not os.path.exists('/usr/to/ner'):
  os.makedirs('/usr/to/ner')
ner.to_disk('/usr/to/ner')
#loading the updated component
from spacy.pipeline import EntityRecognizer
nlp = spacy.load('en', disable=['ner'])
ner = EntityRecognizer(nlp.vocab)
ner.from_disk('/usr/to/ner')
nlp.add_pipe(ner)
#final test
doc = nlp(u'I need a taxi to Festy.')
for ent in doc.ents:
  print(ent.text, ent.label_)
