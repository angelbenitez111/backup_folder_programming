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
    # La conexion conla base de datos no se cierra de manera automatica, igual se tiene que realizar .close.
    with conexion:
    # /cursor = conexion.cursor()/
        # creando un cursor (nos permite ajecutar sentencias sql)
        # El with nos permite cerrarel cursor de manera automatica
        with conexion.cursor() as cursor:
            sentencia ='SELECT * FROM persona'

            # ejecutamos la sentencia
            cursor.execute(sentencia)

            # recuperamos todos los registros de la sentencia que se ha ejecutado
            registros = cursor.fetchall()

            # imprimimos
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    # Si llegamos a hacerlo sin el bloque with tendriamos que cerrar el cursor de manera manual
    # cursor.close()
    conexion.close()
