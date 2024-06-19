import time
from bs4 import BeautifulSoup
import pandas as pd
# Configuration pandas for view all the colum and without truncating cell contents.
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)

# Leer el contenido del archivo HTML
file_path = (r'C:\Users\abenitez\Desktop\backup_folder_programming\python\personales\lista_de_pc_pentium\Informe sobre '
             r'el registro de hardware.html')
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Analizar el contenido del HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrar la tabla con la clase "TABLE_COL"
table = soup.find('table', class_='DATA_TABLE DATA_TABLE_WO_TOTAL')

# Extraer los datos de la tabla
rows = table.find_all('tr')
data = []

for row in rows:
    cols = row.find_all(['td', 'th'])
    # col.grt_tex(strip=True)  extrae todo el texto dentro deuna etiqueta

    cols = [col.get_text(strip=True) for col in cols]
    data.append(cols)
    # strip=True: Este argumento adicional elimina cualquier espacio en blanco inicial y final alrededor del texto extraído. Es equivalente a llamar a strip() en el texto resultante.


for dat in data:
    print(dat)

# Crear un DataFrame de pandas
df = pd.DataFrame.from_dict({i: dat for i, dat in enumerate(data)}, orient='index').transpose()

print(df)


# Exportar el DataFrame a un archivo Excel
now = time.localtime()
timestamp = time.strftime("%y_%m_%d %H_%M", now)
filename = f"INVENTARIO PC {timestamp}.csv"


# df2.to_csv('contactos.csv', index=False)
# df.to_csv(filename, index=False, encoding='utf-8-sig')


