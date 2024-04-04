# programa que usa el paquete cuentas

from cuentas.miscuentasclasses import CuentaCorriente
from cuentas.miscuentasclasses import CantidadException

try:
    cc1 = CuentaCorriente(1, "Aurelio", 10000, 1000)
    print(cc1)
    cc2 = CuentaCorriente(2, "Pedro", -10000, 1000)
    print(cc2)
except CantidadException as e:
    print(e)

try:
    cc1.retirar(2000)
    print(cc1)
    cc1.retirar(20000)
    print(cc1)
except CantidadException as e:
    print(e)