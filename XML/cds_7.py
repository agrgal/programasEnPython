# coding: utf-8

from xml.dom import minidom, Node

def scanNode(node, level = 0):
    msg = node.__class__.__name__
    texto=""
    if node.nodeType == Node.ELEMENT_NODE:
        msg += ", tag: " + node.tagName
    elif node.nodeType == Node.TEXT_NODE:
		texto = ": "+node.data
    print " " * level * 4, msg, texto
    if node.hasChildNodes:
        for child in node.childNodes:
            scanNode(child, level + 1)
            
doc = minidom.parse('cd_catalogo.xml') 
scanNode(doc)
