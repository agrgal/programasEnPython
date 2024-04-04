# Llamando a module1
""" Si llamo a import module1 sin más, el código ejecutable se ejecuta"""

# import module1 # este no tiene la precaución de que no se ejecute cuando se llamado como MóDULO

import module1_BIS  # este tiene la precaución de que no se ejecute su código que está dentro
#  de la claúsula if __name__ == '__main__':
#  porque su nombre sería module1_BIS llamándolo así.
module1_BIS.f1()
print(module1_BIS.__name__)
