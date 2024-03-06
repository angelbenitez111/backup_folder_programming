import psycopg2 as bd

# Conexion a base de datos
conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    # Lo recomendable es tener el autocommit en false o utilizar el with
    # conexion.autocommit = False <estado por defecto>
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('Maria', 'Esparza', 'mesparza@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Juan Carlos', 'Perez', 'jcjuarez@mail.com', 1)
    cursor.execute(sentencia, valores)

    print('Se hizo commit')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo rollback de la transaccion: {e}')

finally:
    conexion.close()
