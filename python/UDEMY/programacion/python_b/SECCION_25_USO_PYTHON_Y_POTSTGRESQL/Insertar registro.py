import psycopg2

# Coneccion a base de datos
conexion = psycopg2.connect(
    # Usuario por defecto de postges
    user='postgres',
    password='admin',
    # Nuestra ip de manera local
    host='127.0.0.1',
    # Puerto por defecto
    port='5432',
    database='test_db'
)
try:
    # La conexion con la base de datos no se cierra de manera automatica, igual se tiene que realizar .close.
    with conexion:
        # /conexion = conexion.cursor()/
        # creando un cursor (nos permite ajecutar sentencias sql)
        # El with nos permite cerrar el cursor de manera automatica
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            """
            - Esto es para insertar un solo valor - 
            valores = ('Carlos', 'Lara', 'clara@mail.com')
            cursor.execute(setencia, valores)
            """
            valores = (
                ('Marcos', 'Cantu', 'mcantu@mail.com'),
                ('Cesar', 'Davalos', 'csavalos@mail.com'),
                ('Juan', 'Candia', 'jcandia@mail.com')
            )

            # cambiamos el .execute por .excecutemany para poder agregar varios registros.
            cursor.executemany(sentencia, valores)

            # conexion.commit() <Se guardan los cambios - Esto se realiza de manera automatica con with>

            # con .rowcount vemos cuantos registros fueron afectados
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close()
