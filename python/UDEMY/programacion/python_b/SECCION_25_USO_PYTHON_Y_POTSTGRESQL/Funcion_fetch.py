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
        # /conexion = conexion.cursor()/
        # creando un cursor (nos permite ajecutar sentencias sql)
        # El with nos permite cerrarel cursor de manera automatica
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s' # %s placeholder o parametro posicional
            id_persona = input('Proporciona el valor de id_persona: ')
            # ejecutamos la sentencia y determinamos con la tupla, cual registro queremos que nos devuelva
            cursor.execute(sentencia, (id_persona,))

            # recuperamos solo un registro de la sentencia que se ha ejecutado
            registros = cursor.fetchone()

            # imprimimos
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    # Si llegamos a hacerlo sin el bloque with tendriamos que cerrar el cursor de manera manual
    # cursor.close()
    conexion.close()
