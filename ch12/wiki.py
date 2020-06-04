import spacy
import wikipedia
def wiki(doc):
  for t in doc:
    if t.dep_ == 'pobj' and (t.pos_ == 'NOUN' or t.pos_ == 'PROPN'):
      phrase = t.lemma_
      return [phrase,1]
  for t in reversed(doc):
    if t.dep_ == 'nsubj' and (t.pos_ == 'NOUN' or t.pos_ == 'PROPN'):
      phrase = t.text + ' ' + t.head.text
      return [phrase,2]
  for t in reversed(doc):
    if t.dep_ == 'dobj' and (t.pos_ == 'NOUN' or t.pos_ == 'PROPN'):
      phrase = t.head.text + 'ing' + ' ' + t.text
      return [phrase,3]
  return False

def main():
  nlp = spacy.load('en')
  doc = nlp(u"Do you know what a horse eats?")
  phrase = wiki(doc)
  if phrase != False:
    article = wikipedia.page(phrase[0].split()[0])
    doc = nlp(article.content)
  else:
    return
  if phrase[1]== 1: 
    print(list(doc.sents)[0])
  if phrase[1]== 2: 
    docphrase = nlp(phrase[0])
    for sent in doc.sents:
      for t in sent:
        if t.lemma_ == docphrase[0].lemma_ and t.head.lemma_ == docphrase[1].lemma_:
          print(sent.text)
          return
if __name__ == '__main__':
    main()
