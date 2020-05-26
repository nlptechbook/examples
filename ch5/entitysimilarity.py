import spacy
nlp = spacy.load('en')
#first sample text
doc1 = nlp(u'Google Search, often referred to as simply Google, is the most used search engine nowadays. It handles a huge number of searches each day.')
#second sample text
doc2 = nlp(u'Microsoft Windows is a family of proprietary operating systems developed and sold by Microsoft. The company also produces a wide range of other software for desktops and servers.')
#third sample text
doc3 = nlp(u"Titicaca is a large, deep, mountain lake in the Andes. It is known as the highest navigable lake in the world.")
docs = [doc1,doc2,doc3]
spans = {}
for j,doc in enumerate(docs):
 named_entity_span = [doc[i].text for i in range(len(doc)) if
 doc[i].ent_type != 0]
 print(named_entity_span)
 named_entity_span = ' '.join(named_entity_span)
 named_entity_span = nlp(named_entity_span)
 spans.update({j:named_entity_span})
print('doc1 is similar to doc2:',spans[0].similarity(spans[1]))
print('doc1 is similar to doc3:',spans[0].similarity(spans[2]))
print('doc2 is similar to doc3:',spans[1].similarity(spans[2]))
