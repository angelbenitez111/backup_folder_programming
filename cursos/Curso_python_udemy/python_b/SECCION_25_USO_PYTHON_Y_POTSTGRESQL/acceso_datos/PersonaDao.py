from Conexion import Conexion
from Persona import Persona
from logger_base import log


class PersonaDao:
    """
    DAO (Data access Object)
    CRUD (Create-Read-Update-Delete)
    """

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                # Ejecuta el sql
                cursor.execute(cls._SELECCIONAR)
                # Guardamos el registro.
                registros = cursor.fetchall()
                personas = []

                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas

    @classmethod
    # Have a transaction
    def insertar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f"Persona insertada: {persona}")
                # Devolvemos los valores insertados
                return cursor.rowcount



    @classmethod
    def actualizar(cls, persona):
        pass

    @classmethod
    def eliminar(cls, persona):
        pass

if __name__ == "__main__":
    # Insertamos un objeto
    persona1 = Persona(nombre='Pedro', apellido='Peralta', email='pperalta@mail.com')
    personas_insertadas = PersonaDao.insertar(persona1)
    log.debug(f"Personas insertadas: {personas_insertadas}")

    #Seleccionar objeto
    personas = PersonaDao.seleccionar()
    for persona in personas:
        log.debug(persona)
