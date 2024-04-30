import pandas as pd


# Funciones
def chr_int(a):
    """ Si es un número, lo devuelve. Si no devuelve -1 """
    if a.strip().isdigit():
        return int(a)
    else:
        return -1


file = open('adult.data', 'r')  # apertura del fichero

datos = []  # Base de datos
n = 0  # recuento de datos
for i in file:  # por cada fila del fichero de datos
    fila = i.split(",")  # divide en trozo las filas
    for j in range(0, len(fila)):  # por cada trozo de una fila…
        fila[j] = fila[j].strip()  # quito espacios innecesarios al principio y al final
        if chr_int(fila[j]) > -1:  # si es un número
            fila[j] = int(fila[j])  # lo almacena como entero.
    n += 1
    try:
        datos.append(fila)
    except IndexError as e:
        print("Fin de fichero")

# En pantalla algunos datos.
for algunos in datos[0:10]:
    print(algunos)

# Se construye un dataframe en pandas
df = pd.DataFrame(
    datos)  # datos es una lista de listas, cada una con un registro. En el programa se han quitado espacios a cada dato leído del fichero, se han convertido en enteros los que eran números.
df.columns = ['edad', 'tipo de empleado', 'fnlwgt', 'educación', 'educación_n', 'estado civil', 'ocupación', 'relación',
              'carrera', 'sexo', 'ganancias', 'pérdidas', 'horas semana', 'país', 'ingresos']
print(df.shape)
contar = df.groupby('país').size()  # agrupo por países, y calculo cuántas filas hay por cada país
print(contar.head())  # muestro las cinco primeras.

# separamos los data frames por sexo, y por sexo y por nivel de ingresos
mdf = df[df['sexo'] == 'Male']
wdf = df[df['sexo'] == 'Female']
mdf1 = df[(df['sexo'] == 'Male') & (df['ingresos'] == '>50K')]
wdf1 = df[(df.sexo == 'Female') & (df.ingresos == '>50K')]
print(mdf1.head(), wdf1.head())
