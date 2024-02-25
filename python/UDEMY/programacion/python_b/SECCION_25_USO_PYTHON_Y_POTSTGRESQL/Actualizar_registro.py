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
            sentencia = 'UPDATE persona SET nombre =%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores=(
                ('Ivonne', 'Gutierres', 'igutierres@mail.com', '7'),
                ('pepito', 'Juarez', 'pjuarez@mail.com', '8'),
                ('Ale', 'britez', 'abritez@mail.com', '9')
            )

            # Si solo fuera uno podemos utilizar .execute y listo
            cursor.executemany(sentencia, valores)

            # con .rowcount vemos cuantos registros fueron actualizados
            registros_actuatilizados = cursor.rowcount
            print(f'Registros insertados: {registros_actuatilizados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close()
