# Locate directory of Namespace

# importing random module
from rdflib import  random
  
# importing the os module
import os
  
# storing the path of modules file 
# in variable file_path
file_path = random.__file__
  
# storing the directory in dir variable
dir = os.path.dirname(file_path)
  
# printing the directory
print(dir)

# Copy _SPR there

line = '        self.bind("xsd", XSD)'

line = 'from rdflib.namespace._XSD import XSD'