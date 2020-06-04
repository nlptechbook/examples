train_exams = [
 ('Could you send a taxi to Solnce?', {
 'entities': [(25, 32, 'GPE')]
 }),
  ('Is there a flat rate to the airport from Solnce?', {
   'entities': [(41, 48, 'GPE')]
 }),
  ('How long is the wait for a taxi right now?', {
   'entities': []
 })
]

import spacy
nlp = spacy.load('en')
doc = nlp(u'Could you pick me up at Solnce?')
for ent in doc.ents:
  print(ent.text, ent.label_)

doc = nlp(u'Could you send a taxi to Solnce? I need to get to Google. Could you send a taxi an hour later?')
districts = ['Solnce', 'Greenwal', 'Downtown']
for sent in doc.sents:
  entities = []
  for token in sent:
    if token.ent_type != 0:
      start = token.idx - sent.start_char
      if token.text in districts:
        entity = (start, start + len(token), 'GPE')
      else:
        entity = (start, start + len(token), token.ent_type_)
      entities.append(entity)
  tpl = (sent.text, {'entities': entities})
  train_exams.append(tpl) 
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
nlp.disable_pipes(*other_pipes)
import random
from spacy.util import minibatch, compounding
optimizer = nlp.entity.create_optimizer()
for i in range(25):
  random.shuffle(train_exams)
  max_batch_size = 3
  batch_size = compounding(2.0, max_batch_size, 1.001)
  batches = minibatch(train_exams, size=batch_size)
  for batch in batches:
    texts, annotations = zip(*batch)
    nlp.update(texts, annotations, sgd=optimizer)
ner = nlp.get_pipe('ner')
ner.to_disk('/usr/to/ner')
