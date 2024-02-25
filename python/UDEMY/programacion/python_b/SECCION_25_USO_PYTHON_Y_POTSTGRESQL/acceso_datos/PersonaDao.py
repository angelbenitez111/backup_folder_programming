from Conexion import Conexion
from Persona import Persona

class PersonaDao:
    SELECCIONAR = 'SELECT * FROM persona WHERE id_persona = %s'
    INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE persona SET nombre=%s, email=%s WHERE id_persona=%s'
    ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        try:
            with Conexion.obtenerConexion():
                with Conexion.obtenerCursor() as cursor:
                    id_persona = input('Proporciona el valor de id_persona: ')
                    cursor.execute(cls.SELECCIONAR, id_persona)
                    # recuperamos solo un registro de la sentencia que se ha ejecutado
                    registros = cursor.fetchone()
                    # imprimimos
                    print(registros)
        except Exception as e:
            print(f'Ocurrio un error: {e}')

        finally:
            Conexion.obtenerConexion().close()

    @classmethod
    def insertar(cls, persona):
        try:
            with Conexion.obtenerConexion():
                with Conexion.obtenerCursor() as cursor:
                    pass

        except Exception as e:
            print(f'Ocurrio un error: {e}')

        finally:
            Conexion.obtenerConexion().close()


    @classmethod
    def actualizar(cls, persona):
        pass

    @classmethod
    def eliminar(cls, persona):
        pass
