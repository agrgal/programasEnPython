# *-* coding:utf-8 *-*

# Código 11.3: genera_saludo.py: Genera el archivo saludo.py
saludo = open("hola.txt", "a")
saludo.write("""
Y mejor que va a escribir
""")
saludo.close()

