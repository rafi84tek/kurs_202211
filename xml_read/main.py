"""
XML
"""

from xml.dom.minidom import parse
import xml.etree.ElementTree as ET

dom = parse("dane.xml")
name = dom.getElementsByTagName('name')
kod = dom.getElementsByTagName('kod')
url = dom.getElementsByTagName('url')

#poniżej zwrócony został tekst, bez elementów w TAGach
print(" ".join(t.nodeValue for t in name[0].childNodes if t.nodeType==t.TEXT_NODE))
print(" ".join(t.nodeValue for t in kod[0].childNodes if t.nodeType==t.TEXT_NODE))
print(" ".join(t.nodeValue for t in url[0].childNodes if t.nodeType==t.TEXT_NODE))
print(" ".join(t.nodeValue for t in url[1].childNodes if t.nodeType==t.TEXT_NODE))
print(" ".join(t.nodeValue for t in url[2].childNodes if t.nodeType==t.TEXT_NODE))

print("-------------------------------------")

try:
    tree = ET.parse("dane.xml")
    root = tree.getroot()
    print(root)
    for child in root:
        print(f"tag: {child.tag}, atrybut: {child.attrib}")

    print(root[0].text) #druk elementu 0 z roota
except:
    print("Element nie istnieje")

