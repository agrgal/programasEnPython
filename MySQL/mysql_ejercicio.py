# coding: utf-8

import MySQLdb
from xml.dom import minidom, Node
import json

# datos IMPRESCINDIBLES de conexión 
DB_HOST = 'localhost'   		# -> servidor
DB_USER = 'root' 				# -> usuario administrador o con permisos GRANT
DB_PASS = 'mipassword' 				# -> contraseña de usuario
DB_NAME = 'callejero_madrid' 	# -> Nombre de la base de datos

# Función que conecta y ejecuta una consulta 
def run_query(query=''): 
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
 
    conn = MySQLdb.connect(*datos,charset='utf8') # Conectar a la base de datos, con el juego de caracteres UTF-8
    cursor = conn.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 
 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos 
        data = None 
 
    cursor.close()                 # Cerrar el cursor 
    conn.close()                   # Cerrar la conexión 
 
    return data

# ==================
# programa principal
# ==================

# Acceso a la base de datos
buscar = "SELECT `Literal`, `Fecha del alta de la denominacion de via` AS fecha FROM callejero ORDER BY fecha LIMIT 1000"
# Para que no se haga muy largo conviene poner LIMIT 100
datos = run_query(buscar)
# print datos

# ==================
# Crear documento XML
# ==================
doc = minidom.Document() #--> Crear un documento xml
doc.appendChild(doc.createComment("Creando documento de callejero con  XML")) #-> Escribir comentario

callejero = doc.createElement('Callejero') # --> Crear elemento dentro del documento
doc.appendChild(callejero)

for i in datos:
	# print i[0],i[1]
	# Nombre de la calle
	calle = doc.createElement('Calle')
	callejero.appendChild(calle)
	nombre = doc.createElement('Nombre')
	nombre.appendChild(doc.createTextNode(i[0].rstrip(' '))) # --> recorta por lña derecha los espacios
	calle.appendChild(nombre)
	# Fecha de alta de denominación de la vía
	fecha = doc.createElement('Fecha')
	fecha.appendChild(doc.createTextNode(i[1]))
	calle.appendChild(fecha)

print doc.toprettyxml(indent ='   ')

# Guardar XML
fichero = open("callejero.xml","w")
fichero.write(doc.toprettyxml(encoding="utf-8"))
fichero.close()

# ====================
# Crear documento JSON
# ====================

# Crear un diccionario...
calle = []
dic = {}
for i in datos:
	dic["Nombre"] = i[0].rstrip(' ')
	dic["Fecha"] = i[1]
	calle.append(dic)
	dic={} # vaciar el dic
	# print i[0],i[1]

callejero = {}
callejero["Callejero"] = calle

callejero_str= json.dumps(callejero, ensure_ascii=False, separators=(',',':')) #--> de forma compacta
# -> ensure_ascii = False, asegura que se graba en utf-8

archivo = open("callejero.json.txt","w")
# archivo.write(callejero_str.encode("utf-8")) # -> Junto con ensure_ascii
archivo.write(callejero_str.encode("utf-8")) # -> Junto con ensure_ascii
archivo.close()

archivo = open("callejero.json.txt","r")
callejero_recibido=json.loads(archivo.read())
archivo.close()

tab = " " * 1 # -> Leyendo de esta forma sí se obtiene en UTF-8
for lista in callejero_recibido["Callejero"]:
	for clave, valor in lista.items():
		print tab, clave, valor
		


print "Proceso terminado"

