# coding: utf-8

from xml.dom import minidom                                        

xmldoc = minidom.parse('cd_catalogo.xml')     
 

print xmldoc.__class__                               
print xmldoc.__class__.__name__

plist = xmldoc.getElementsByTagName("TITULO")  
print plist 
print plist[0].toxml()                               
print plist[1].toxml() 
print plist[2].toxml()                                                             

