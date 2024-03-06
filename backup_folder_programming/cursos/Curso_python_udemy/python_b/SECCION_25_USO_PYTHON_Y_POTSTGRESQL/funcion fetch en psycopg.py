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
            # IN para indicar que podemos procesar varios registros
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s' # %s placeholder o parametro posicional
            entrada = input('Proporciona los id\'s a buscar: (separado por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)
            #llaves_primarias = ((1,2,3),)

            # ejecutamos la sentencia y determinamos con la tupla, cual registro queremos que nos devuelva
            cursor.execute(sentencia, llaves_primarias)

            # recuperamos solo un registro de la sentencia que se ha ejecutado
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    # Si llegamos a hacerlo sin el bloque with tendriamos que cerrar el cursor de manera manual
    # cursor.close()
    conexion.close()
