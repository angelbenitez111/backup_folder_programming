import pandas as pd
import re
# Configuration pandas for view all the colum and without truncating cell contents.
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)

# Read the file
df = pd.read_csv('usuarios.csv', delimiter=';', skipinitialspace=True)
columnas = ["Nombre", "Mail"]

# Create one clean dataframe
df2 = pd.DataFrame(columns=columnas)

# print(df.head(10))

"""
num_filas = df.shape[0]
num_columnas = df.shape[1]

print(num_columnas)
print(num_filas)
"""
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

p_before_semicolon = r"^([^;]*)"

patron_user_nombre = r"^([^;]*)"
patron_group_nombre = r'^;(.+)'

for i, row in enumerate(df.iterrows()):
    cont += 1
    fila = df.iloc[i]

    # is a  group
    if (df.iloc[i, 0] == 7) and (df.iloc[i, 2] != 'public-folders') and df.iloc[i, 2] != 'private_aesaseguros.com.py' and (df.iloc[i, 2] != 'teamchat_it'):
        # Obtaining mail
        aux_mail = f'{re.search(p_before_semicolon, df.iloc[i, 2]).group(1)}@aesaseguros.com.py'

        # Obtaining name
        if df.iloc[i, 4] == ";":
            aux_name = f'{df.iloc[i, 2]}'
            # print(f'[{i}]{aux_name}:  {aux_mail}')
        else:
            aux_name = f'{re.search(patron_group_nombre, df.iloc[i, 4]).group(1)}'
            # print(f'[{i}]{aux_name}:  {aux_mail}')

        new_row = pd.DataFrame({'Nombre': [aux_name], 'Mail': [aux_mail]})
        # Usar pd.concat para agregar la nueva fila
        df2 = pd.concat([df2, new_row], ignore_index=True)
        # print(aux_name)

    # if is a person
    elif df.iloc[i, 0] == 0:
        # Obtaining name
        aux_name = f'{re.search(patron_user_nombre, df.iloc[i, 4]).group(1)}'
        # print(aux_name)

        # Obtaining mail
        aux_mail = f'{re.search(p_before_semicolon, df.iloc[i, 2]).group(1)}@aesaseguros.com.py'
        # print(aux_mail)
        new_row = pd.DataFrame({'Nombre': [aux_name], 'Mail': [aux_mail]})
        # Usar pd.concat para agregar la nueva fila
        df2 = pd.concat([df2, new_row], ignore_index=True)
    else:
        pass
print(df2)
# df2.to_csv('contactos.csv', index=False)
df2.to_csv('contactos.csv', index=False, encoding='utf-8')
