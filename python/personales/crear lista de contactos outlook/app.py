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

import pandas as pd
import re

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

# Leemos el archivo CSV
df = pd.read_csv('usuarios.csv', delimiter=';', skipinitialspace=True)

print(df.head())

num_filas = df.shape[0]
num_columnas = df.shape[1]


for i, row in df.iterrows():
    for j, cell in enumerate(row):
        # Asegurarse de que el valor de la celda es una cadena
        cell = str(cell)
        # Extraer y imprimir la dirección de correo electrónico
        email = extraer_email(cell)
        if email:
            print(email)
