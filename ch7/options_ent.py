import spacy
nlp = spacy.load('en')
doc = nlp(u"In 2011, Google launched Google +, its fourth foray into social networking.")
doc.user_data['title'] = "An example of an entity visualization"
from spacy import displacy
options = {'ents': ["ORG", "PRODUCT", "DATE"], 'colors': {"ORG": "aqua","PRODUCT": "aqua"}}
displacy.serve(doc, style='ent', options=options)
