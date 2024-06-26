from logger_base import log
from Conexion import Conexion


class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Inicio del método with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipos_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('se ejecuta método __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(
                f'Ocurrio una excepción, se hace rollback: {valor_excepcion} {tipos_excepcion} {detalle_excepcion}')
        else:
            self._conexion.commit()
            log.debug('commit de la transaccion')
        # se cierra la conexion
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == "__main__":
    with CursorDelPool() as cursor:
        log.debug('Dentro del with')
        # realizamos una consulta
        cursor.execute('SELECT * FROM PERSONA')
        log.debug(cursor.fetchall())
