from distutils.core import setup
from Cython.Build import cythonize
import numpy
setup(name='spacy text app',
 ext_modules=cythonize("spacytext.pyx", language="c++"),
  include_dirs=[numpy.get_include()]
   )
