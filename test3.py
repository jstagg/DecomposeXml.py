#!python
# 
# 
# With thanks to:
# Scott Robinson (https://stackabuse.com/reading-and-writing-xml-files-in-python/)
# 
# Python docs:
# https://docs.python.org/3/library/xml.etree.elementtree.html
# 

import xml.etree.ElementTree as ET
import re

tree = ET.parse('amx.xml')
root = tree.getroot()

# Order Header
for el in root.iter():
    ET.dump(el)

# Order Footer

# Order lines
#for OrderLine in root.iter('OrderLine'):
#    ET.dump(OrderLine)


# -30- #