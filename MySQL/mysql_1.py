# coding: utf-8
import MySQLdb

# datos IMPRESCINDIBLES de conexión 
DB_HOST = 'localhost'   		# -> servidor
DB_USER = 'root' 				# -> usuario administrador o con permisos GRANT
DB_PASS = '7171' 				# -> contraseña de usuario
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

# programa principal
datos = run_query("SELECT Literal from callejero LIMIT 100") # -> Nombre de una tabla de la base de datos.
# print datos
for i in datos:
	print i[0]
