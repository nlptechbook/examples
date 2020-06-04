sent = {
 "words": [
   {"text": "I", "tag": "PRON"},
   {"text": "want", "tag": "VERB"},
   {"text": "a", "tag": "DET"},
   {"text": "Greek", "tag": "ADJ"},
   {"text": "pizza", "tag": "NOUN"}
 ],
 "arcs": [
   {"start": 0, "end": 1, "label": "nsubj", "dir": "left"},
   {"start": 2, "end": 4, "label": "det", "dir": "left"},
   {"start": 3, "end": 4, "label": "amod", "dir": "left"},
   {"start": 1, "end": 4, "label": "dobj", "dir": "right"}
 ]
}
from spacy import displacy
displacy.serve(sent, style="dep", manual=True)
