import spacy
import sys
def find_chunk(doc):
  chunk = ''
  for i,token in enumerate(doc):
    if token.dep_ == 'dobj':
      shift = len([w for w in token.children])
      #print([w for w in token.children])
      chunk = doc[i-shift:i+1]
      break
  return chunk
def determine_question_type(chunk):
  question_type = 'yesno'
  for token in chunk:
    if token.dep_ == 'amod':
      question_type = 'info'
  return question_type

def generate_question(doc, question_type):
  sent = ''
  for i,token in enumerate(doc):
    if token.tag_ == 'PRP' and doc[i+1].tag_ == 'VBP':
      sent = 'do ' + doc[i].text
      sent = sent + ' ' + doc[i+1:].text
      break
  doc=nlp(sent)
  for i,token in enumerate(doc):
    if token.tag_ == 'PRP' and token.text == 'I':
      sent = doc[:i].text + ' you ' + doc[i+1:].text
      break
  doc=nlp(sent)
  if question_type == 'info':
    for i,token in enumerate(doc):
      if token.dep_ == 'dobj':
        sent = 'why ' + doc[:i].text + ' one ' + doc[i+1:].text
        break
  if question_type == 'yesno':
    for i,token in enumerate(doc):
      if token.dep_ == 'dobj':
        sent = doc[:i-1].text + ' a red ' + doc[i:].text
        break
  doc=nlp(sent)
  sent = doc[0].text.capitalize() +' ' + doc[1:len(doc)-1].text + '?'
  return sent
#the main code
if len(sys.argv) > 1:
  sent = sys.argv[1]
  nlp = spacy.load('en')
  doc = nlp(sent)
  chunk = find_chunk(doc)
  if str(chunk) == '':
    print('The sentence does not contain a direct object.')
    sys.exit()
  question_type = determine_question_type(chunk)
  question = generate_question(doc, question_type)
  print(question)
else:
  print('You did not submit a sentence!')

