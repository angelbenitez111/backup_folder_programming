# import pandas as pandas
"""
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
"""
"""
num_filas = df.shape[0]
num_columnas = df.shape[1]

print(num_columnas)
print(num_filas)
"""
"""
# Create your own labels:
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
"""
"""
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
"""

"""
# Create a Series using only data from "day1" and "day2":
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

"""

"""
Check the number of maximum returned rows:

import pandas as pd

print(pd.options.display.max_rows)

"""

"""
Get a quick overview by printing the first 10 rows of the DataFrame:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))
"""

"""
# Print the last 5 rows of the DataFrame:
print(df.tail()) 
"""

"""
# Print information about the data:

print(df.info()) 
"""

"""
Return a new Data Frame with no empty cells:

import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())

"""
# Load a comma separated file (CSV file) into a DataFrame:


"""
def extraer_email(texto):
    # Patrón para buscar direcciones de correo electrónico
    patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # Buscar la dirección de correo en el texto
    match = re.search(patron_email, texto)
    # Si se encuentra, devolver la dirección, si no, devolver None
    if match:
        return match.group(0)
    elif texto != "nan" and not(re.search(r"^aesaseguros\.com\.py,", texto)):
        return texto + "@aesaseguros.com.py"
    else:
        return None

    # return match.group(0) if match else texto
"""
import pandas as pd
import re

# Configurar pandas para mostrar todas las columnas y sin truncar el contenido de las celdas
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)

# Leemos el archivo CSV
df = pd.read_csv('usuarios.csv', delimiter=';', skipinitialspace=True)
columnas = ["Nombre", "mail"]
df2 = pd.DataFrame(columns=columnas)

print(df.head(10))

num_filas = df.shape[0]
num_columnas = df.shape[1]

print(num_columnas)
print(num_filas)

"""
colum segundo for
fila primer for

0 = type
1 = id
2 = alias
3 = domain
4 = name
5 = mailbox


"""
aux_name = ""
aux_mail = ""
cont = 0
# for i, row in df.iterrows():

p_before_semicolon = r"^([^;]*)"

patron_user_nombre = r"^([^;]*)"
patron_group_nombre = r'^;(.+)'

for i, row in enumerate(df.iterrows()):
    cont += 1
    fila = df.iloc[i]

    # Si es un grupo
    if (df.iloc[i, 0] == 7) and (df.iloc[i, 2] != 'public-folders') and df.iloc[i, 2] != 'private_aesaseguros.com.py':
        # Obtaining mail
        aux_mail = f'{re.search(p_before_semicolon, df.iloc[i, 2]).group(1)}@aesaseguros.com.py'

        # Obtaining name
        if df.iloc[i, 4] == ";":
            aux_name = f'{df.iloc[i, 2]}'
        else:
            aux_name = f'{re.search(patron_group_nombre, df.iloc[i, 4]).group(1)}'

        print(aux_name)
        # print(f'{aux_mail.group(1)}@aesaseguros.com.py --- '

    # Si es una persona
    elif df.iloc[i, 0] == 0:
        aux_name = re.search(patron_user_nombre, df.iloc[i, 4])
        print(f'\n- Nombre: {aux_name.group(1)}')

        aux_mail = re.search(p_before_semicolon, df.iloc[i, 2])
        print(f'[{i}]{aux_mail.group(1)}@aesaseguros.com.py')

"""
    for j, cell in enumerate(row):
        # filtramos el tipo de mail
        # grupos
        if j == 0 and ():
"""

#        print(row, "------------", type(row))
#        print(f"[{i}, {j} celda: {cell}]")
