#!python
# 
# 
# With thanks to:
# Scott Robinson (https://stackabuse.com/reading-and-writing-xml-files-in-python/)
# 

from xml.dom import minidom

# parse an xml file by name
mydoc = minidom.parse('amx.xml')

Lines = mydoc.getElementsByTagName('OrderLine')

# all item attributes
print('\nAll attributes:')
for elem in Lines:
    print(elem.attributes['SequenceNum'].value)

# -30- #