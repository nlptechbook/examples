from cymem.cymem cimport Pool
from spacy.tokens.doc cimport Doc
from spacy.structs cimport TokenC
from spacy.typedefs cimport hash_t

cdef struct DocStruct:
  TokenC* c
  int length

cdef int counter(DocStruct* doc, hash_t tag):
  cdef int cnt = 0
  for c in doc.c[:doc.length]:
    if c.tag == tag:
      cnt += 1
  return cnt 

cpdef main(Doc mydoc):
  cdef int cnt
  cdef Pool mem = Pool()
  cdef DocStruct* doc_ptr = <DocStruct*>mem.alloc(1, sizeof(DocStruct))
  doc_ptr.c = mydoc.c
  doc_ptr.length = mydoc.length
  tag = mydoc.vocab.strings.add('PRP')
  cnt = counter(doc_ptr, tag)
  print(doc_ptr.length)
  print(cnt)
