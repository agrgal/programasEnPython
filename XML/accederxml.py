from xml.dom import minidom

xmldoc = minidom.parse('cd_catalogo.xml')

cNodes = xmldoc.childNodes

# print cNodes[1].toxml()

nList = cNodes[0].getElementsByTagName("CD")
for node in nList:
    eList = node.getElementsByTagName("TITULO")
    # for e in eList:
    #   print e.toxml()

nList = cNodes[0].getElementsByTagName("CD")
for node in nList:
    eList = node.getElementsByTagName("ARTISTA")
    # for e in eList:
      #  print e.toxml()

def printNodes (nList, level):
    for node in nList:
        print ("  ")*level, node.nodeName, node.nodeValue
        printNodes(node.childNodes, level+1)

printNodes(xmldoc.childNodes, 0)
