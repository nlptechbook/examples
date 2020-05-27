import spacy
from spacy.matcher import Matcher
nlp = spacy.load("en")
matcher = Matcher(nlp.vocab)
pattern = [{"DEP": "nsubj"}, {"DEP": "aux"}, {"DEP": "ROOT"}]
matcher.add("NsubjAuxRoot", None, pattern)
doc = nlp(u"We can overtake them.")
matches = matcher(doc)
for match_id, start, end in matches:
  span = doc[start:end]
  print("Span: ", span.text)
  print("The positions in the doc are: ", start, "-", end)
