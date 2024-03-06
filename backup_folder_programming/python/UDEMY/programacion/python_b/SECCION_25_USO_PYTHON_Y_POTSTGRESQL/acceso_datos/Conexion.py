# pip install psycopg2
import psycopg2

class Conexion:
    DATABASE = 'test_db'
    USERNAME = 'postgres'
    PASSWORD = 'admin'
    DB_PORT = '5432'
    HOST = '127.0.0.1'
    conexion = psycopg2.connect(user=USERNAME, password=PASSWORD, host=HOST, port=DB_PORT, database=DATABASE)
    cursor = conexion.cursor()

    @classmethod
    def obtenerConexion(cls):
        return cls.conexion

    @classmethod
    def obtenerCursor(cls):
        return cls.conexion

    @classmethod
    def cerra(cls):
        cls.cursor.close()


if __name__ == "__main__":
    try:
        with Conexion:
            with Conexion.obtenerCursor() as cursor:
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
        Conexion.obtenerConexion().close()
