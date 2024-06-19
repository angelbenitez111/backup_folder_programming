import pandas as pd
import re
import time

# C:\Program Files\IceWarp\config\accounts.db
# SELECT U_Type, U_ID, U_Alias, U_Domain, U_Name, U_Mailbox FROM Users;

# Configuration pandas for view all the colum and without truncating cell contents.
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)

list_ban_mail = ["Admin,admin@aesaseguros.com.py", "Admin,admin@aesaseguros.com.py", "Fax,fax@aesaseguros.com.py",
                 "Util,util@aesaseguros.com.py", "Fax.Cde,fax.cde@aesaseguros.com.py",
                 "It_helpdesk,it_helpdesk@aesaseguros.com.py", "Info,info@aesaseguros.com.py",
                 "Util2,util2@aesaseguros.com.py", "Para envios desde la Pagina Web,contactoweb@aesaseguros.com.py",
                 "Propuestas - Usa Banco Atlas,propuestas@aesaseguros.com.py", "Infoti,infoti@aesaseguros.com.py"]

# Read the file
df = pd.read_csv('usuarios.csv', delimiter=';', skipinitialspace=True)
columnas = ["Nombre", "Mail"]

# Create one clean dataframe
df2 = pd.DataFrame(columns=columnas)

# print(df.head(10))


"""
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
patron_group_nombre = r'^;(.+)'

for i, row in enumerate(df.iterrows()):
    cont += 1
    fila = df.iloc[i]

    # is a  group
    if not (not (df.iloc[i, 0] == 7) or not (df.iloc[i, 2] != 'public-folders') or not (
            df.iloc[i, 2] != 'private_aesaseguros.com.py') or not (df.iloc[i, 2] != 'teamchat_it')):
        # Obtaining mail
        aux_mail = f'{re.search(p_before_semicolon, df.iloc[i, 2]).group(1)}@aesaseguros.com.py'

        # Obtaining name
        if df.iloc[i, 4] == ";":
            aux_name = f'{df.iloc[i, 2]}'.replace('ñ', 'n')
            # print(f'[{i}]{aux_name}:  {aux_mail}')
        else:
            aux_name = f'{re.search(patron_group_nombre, df.iloc[i, 4]).group(1)}'.replace('ñ', 'n')
            # print(f'[{i}]{aux_name}:  {aux_mail}')

        new_row = pd.DataFrame({'Nombre': [aux_name.title()], 'Mail': [aux_mail]})
        # Usar pd.concat para agregar la nueva fila
        df2 = pd.concat([df2, new_row], ignore_index=True)
        # print(aux_name)

    # if is a person
    elif df.iloc[i, 0] == 0:
        # Obtaining name
        aux_name = f'{re.search(p_before_semicolon, df.iloc[i, 4]).group(1)}'.replace('ñ', 'n')
        # print(aux_name)

        # Obtaining mail
        aux_mail = f'{re.search(p_before_semicolon, df.iloc[i, 2]).group(1)}@aesaseguros.com.py'
        # print(aux_mail)
        new_row = pd.DataFrame({'Nombre': [aux_name.title()], 'Mail': [aux_mail]})
        # Use pd.concat for add a new row
        df2 = pd.concat([df2, new_row], ignore_index=True)
    else:
        pass
print(df2)

now = time.localtime()
timestamp = time.strftime("%y_%m_%d %H_%M", now)
filename = f"contacto {timestamp}.csv"

# df2.to_csv('contactos.csv', index=False)
df2.to_csv(filename, index=False, encoding='utf-8-sig')
