# pip install psycopg2
import psycopg2 as bd
from logger_base import log
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                log.debug(f'Conexión exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener la conexión: {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor
"""
        if cls._conexion is None:
            # Creamos el objeto conexion
            try:
                cls._conexion = db.connect(user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           host=cls._HOST,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                log.debug(f"Conexion exitosa: {cls._conexion}")
                return cls._conexion

            except Exception as e:
                log.debug(f"Ocurrio un excepción obtener la conexion{e}")
                # Terminamos el programa
                sys.exit()

        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f"Se abrió correctamente el cursor: {cls._cursor}")
                return cls._cursor

            except Exception as e:
                log.error(f"Ocurrio un excepción al obtener el cursor {e}")
                sys.exit()

        else:
            return cls._conexion

    @classmethod
    def cerra(cls):
        cls.cursor.close()

"""

if __name__ == "__main__":
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()

    """

    try:
        with Conexion:
            with Conexion.obtenerCursor() as _cursor:
                sentencia = 'DELETE FROM persona WHERE id_persona IN %s'

                entrada = input('Proporciona los id_persona a eliminar (separados por coma): ')
                valor = (tuple(entrada.split(',')),)
                # Si solo fuera uno podemos utilizar .execute y listo
                _cursor.execute(sentencia, valor)

                # con .rowcount vemos cuantos registros fueron actualizados
                registros_actuatilizados = _cursor.rowcount
                print(f'Registros insertados: {registros_actuatilizados}')

    except Exception as e:
        print(f'Ocurrio un error: {e}')

    finally:
        Conexion.obtenerConexion().close()
    """