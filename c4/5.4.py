import requests
import lxml.html
from lxml import etree


html = requests.get('https://www.python.org/').content
tree = lxml.html.document_fromstring(html)
tree2 = lxml.html.fromstring(html)
title = tree.xpath('/html/head/title/text()')
title2 = tree2.xpath('/html/head/title/text()')
print(title)
print(title2)
