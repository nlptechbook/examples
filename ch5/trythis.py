import spacy
nlp = spacy.load('en')
token = nlp(u'fruits')[0]
doc = nlp(u'I want to buy this beautiful book at the end of the week. Sales of citrus have increased over the last year. How much do you know about this type of tree?')
similarity = {}
for i, sent in enumerate(doc.sents):
  noun_span_list = [sent[j].text for j in range(len(sent)) if sent[j].pos_ == 'NOUN']
  noun_span_str = ' '.join(noun_span_list)
  noun_span_doc = nlp(noun_span_str)
  print(noun_span_doc.text)
  noun_similarity = 0
  for t in noun_span_doc:
    if t.similarity(token) > noun_similarity:
      noun_similarity = t.similarity(token)
  similarity.update({i:noun_similarity})
print(similarity)
