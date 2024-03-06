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
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los id_persona a eliminar (separados por coma): ')
            valor = (tuple(entrada.split(',')),)
            # Si solo fuera uno podemos utilizar .execute y listo
            cursor.execute(sentencia, valor)

            # con .rowcount vemos cuantos registros fueron actualizados
            registros_actuatilizados = cursor.rowcount
            print(f'Registros insertados: {registros_actuatilizados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close()
