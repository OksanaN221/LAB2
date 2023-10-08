import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
Valute_dict = {}

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Name':
                if child.firstChild.nodeType == 3:
                    Name = child.firstChild.data
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3:
                    CharCode = str(child.firstChild.data.replace(',', '.'))

    Valute_dict[Name] = CharCode

print(Valute_dict)

xml_file.close()