# 
# Decompose EZPO5
# 

from lxml import etree
from io import StringIO, BytesIO
#from copy import deepcopy

root = etree.parse("amx.xml")
save = root
base = root
line = root

for bad in base.xpath("//OrderLine"):
    bad.getparent().remove(bad)

for element in line.iter():
    print("%s" % element.tag)

with open('output_base.xml', 'wb') as f:
    base.write(f, encoding="utf-8", xml_declaration=True, pretty_print=True)

#with open('output_lines.xml', 'wb') as f:
#    f.write(etree.tostring(lines), encoding="utf-8", xml_declaration=True, pretty_print=True)

# -30- #