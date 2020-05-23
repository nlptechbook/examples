import spacy
nlp = spacy.load('en')
doc = nlp(u'I need a taxi to Festy.')
#initial check
for ent in doc.ents:
  print(ent.text, ent.label_)
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
#final test
doc = nlp(u'I need a taxi to Festy.')
for ent in doc.ents:
  print(ent.text, ent.label_)
