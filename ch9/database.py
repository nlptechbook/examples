def word2int(numword):
  num = 0
  try:
    num = int(numword)
    return num
  except ValueError:
    pass    
  words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight","nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

  for idx, word in enumerate(words):
        if word in numword:
           num = idx 
  return num         
import spacy
nlp = spacy.load('en')
#doc = nlp(u'I want twenty three Chicago pizzas.')
doc = nlp(u'I want two Greek pizzas.')
orderdict ={}
for token in doc:
  if token.dep_ == 'dobj':
    dobj = token
    #print(list(dobj.lefts))
    orderdict.update(product = dobj.lemma_ )    
    for child in dobj.lefts:
      if child.dep_ == 'amod' or child.dep_ == 'compound': 
        orderdict.update(ptype = child.text )
      elif child.dep_ == 'det': 
        orderdict.update(qty = 1 )
      elif child.dep_ == 'nummod': 
        orderdict.update(qty = word2int(child.text))
    break
#print(orderdict)

import json
#print(json.dumps(orderdict))
json_str = json.dumps(orderdict)
#print(json_str)

import mysql.connector
from mysql.connector import errorcode
try:
  cnx = mysql.connector.connect(user='root', password='Mysqlway1!',
                              host='127.0.0.1',
                              database='mybot')
  cursor = cnx.cursor()
  query = ("""INSERT INTO orders (product, ptype, qty)
  SELECT product, ptype, qty FROM
       JSON_TABLE(
         %s,
         "$" 
         COLUMNS(
           qty    INT PATH '$.qty' ERROR ON EMPTY, 
           product   VARCHAR(30) PATH "$.product" ERROR ON EMPTY,
           ptype     VARCHAR(30) PATH "$.ptype" ERROR ON EMPTY
          )
       ) AS jt1""");
  cursor.execute(query, (json_str,))
  cnx.commit()
  print('Successfully sent to the database')
except mysql.connector.Error as err:
  print("Error-Code:", err.errno)
  print("Error-Message: {}".format(err.msg))
finally:
  cursor.close()
  cnx.close() 
