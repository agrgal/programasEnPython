import pandas as pd


# Funciones
def chr_int(a):
    """ Si es un número, lo devuelve. Si no devuelve -1 """
    if a.strip().isdigit():
        return int(a)
    else:
        return 0


file = open('adult.data', 'r')  # apertura del fichero

datos = []  # Base de datos
n = 0  # recuento de datos
for i in file:  # por cada fila del fichero de datos
    fila = i.split(",")  # divide en trozo las filas
    for i in range(0,len(fila)):
        fila[i]=fila[i].strip() # necesario limpiar caracteres espacios en blanco o saltos de línea.
    try:
        datos.append([chr_int(fila[0]),
                      fila[1],
                      chr_int(fila[2]),
                      fila[3],
                      chr_int(fila[4]),
                      fila[5], fila[6], fila[7], fila[8], fila[9],
                      chr_int(fila[10]), chr_int(fila[11]), chr_int(fila[12]),
                      fila[13], fila[14]])
    except IndexError as e:
        print("Fin de fichero")

# En pantalla algunos datos.
for algunos in datos[0:10]:
    print(algunos)

# Se construye un dataframe en pandas
df = pd.DataFrame(datos)
# datos es una lista de listas, cada una con un registro. En el programa se han quitado espacios a cada
# dato leído del fichero, se han convertido en enteros los que eran números.
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
print(mdf.head(), wdf.head())

# Porcentajes. Pág 33. varias formas de verlo.
print("Porcentaje de hombres ({}) en datos ({}): {}%"
      .format(df.shape[0], mdf.shape[0], int(10000 * mdf.shape[0] / df.shape[0]) / 100))
print("Porcentaje de mujeres ({}) en datos ({}): {}%"
      .format(len(wdf), len(df), 10000 * len(wdf) / float(len(df) * 100)))
print("Porcentaje de mujeres con altas ganancias ({}) en datos ({}): {}%"
      .format(len(wdf1), len(df), 10000 * len(wdf1) / float(len(df) * 100)))
print("Porcentaje de hombres con altas ganancias ({}) en datos ({}): {}%"
      .format(len(mdf1), len(df), 10000 * len(mdf1) / float(len(df) * 100)))

# Medias. Pág 34
print("Media de las edades en el dataframe datos: {}".format(df['edad'].mean()))
print("Media de las edades de los hombres: {}".format(mdf['edad'].mean()))
print("Media de las edades de las mujeres: {}".format(wdf['edad'].mean()))
print("Media de las edades de los hombres con altas ganancias: {}".format(mdf1['edad'].mean()))
print("Media de las edades de las mujeres con altas ganancias: {}".format(wdf1['edad'].mean()))

# Varianzas y desviaciones típicas.




