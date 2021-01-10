from xml.dom.minidom import Document
import os

def createDocument():
    return Document()


def createTag(document, name):    
    return document.createElement(name)
    

def addTag(father, tag):
    father.appendChild(tag)


def createAttribute(tag, name, value):
    tag.setAttribute(name, value)


def toFile(document, filename):
    file = open(filename, "w")
    file.write(document.toprettyxml(indent="    "))
    file.close()    


def createLevelTag(document):
    name = raw_input("Introduzca el nombre del nivel: ")
    background = raw_input("Introduzca el nombre con la extension de la imagen de fondo: ")
    level = createTag(document, "level")
    createAttribute(level, "name", name)
    createAttribute(level, "background", "res/images/backgrounds/" + background)
    addTag(document, level)
    return level, name


def createEnemies(father, document):
    print "ENEMIGOS"
    print "Introduzca ahora a los enemigos, teclee end en el nombre para dejar de introducir"
    enemies = createTag(document, "enemies")
    while True:
        name = raw_input("Introduzca el nombre del enemigo: ")
        if name == "end": break
		
        while True:
            x = raw_input("Introduzca la posicion inicial X del enemigo: ")
            if 0 < int(x) < 19: break
            print "ERROR: Vuelva a introducirlo. El valor dado no esta en el rango 1-18"
        
        while True:    
            y = raw_input("Introduzca la posicion inicial Y del enemigo: ")
            if 0 < int(y) < 19: break
            print "ERROR: Vuelva a introducirlo. El valor dado no esta en el rango 1-13"
        pos= x + "," + y
        enemy = createTag(level_file, "enemy")
        createAttribute(enemy, "name", name)
        createAttribute(enemy, "pos", pos)
        addTag(enemies, enemy)
    
    addTag(father, enemies)
        
        
def createYou(father, document):
    print "JUGADOR"
    you = createTag(document, "user")
    x = raw_input("Introduzca la posicion inicial X del jugador: ")
    y = raw_input("Introduzca la posicion inicial Y del jugador: ")
    pos = x + "," + y
    createAttribute(you, "pos", pos)
    addTag(father, you)
    

def createBlocks(father, document):
	print "BLOQUES"
	print "Introduzca ahora los bloques (excepto los del borde), introduzca end para finalizar"
	blocks = createTag(document, "blocks")
	while True:
		while True:
			typeBlock = raw_input("Introduzca el tipo (i=invencible, s=softBlock, end para finalizar): ")
			if typeBlock == "s" or typeBlock == "i" or typeBlock == "end": break
			print "ERROR: Vuelva a introducirlo, el valor no es correcto"
			
		if typeBlock == "end": break
		typeBlock = "softBlock" if typeBlock == "s" else "invencible"
        
		while True:
			x = raw_input("Introduzca la posicion X del bloque: ")
			if 0 < int(x) < 19: break
			print "ERROR: Vuelva a introducirlo. El valor dado no esta en el rango 1-18"
        
		while True:    
			y = raw_input("Introduzca la posicion Y del bloque: ")
			if 0 < int(y) < 19: break
			print "ERROR: Vuelva a introducirlo. El valor dado no esta en el rango 1-13"
        
		pos = x + "," + y
		block = createTag(level_file, "block")
		createAttribute(block, "type", typeBlock)
		createAttribute(block, "pos", pos)
		addTag(blocks, block)
    
	addTag(father, blocks)

    
    
print "#########    LEVEL GENERATOR    #########"
level_file = createDocument()
level, name = createLevelTag(level_file)
createYou(level, level_file)
createEnemies(level, level_file)
createBlocks(level, level_file)
toFile(level_file, os.path.join("data/levels", name + ".xml"))
print "ARCHIVO", (name + ".xml"), "GENERADO"
print "Pulse ENTER para finalizar..."
raw_input()
