from Conexion import Conexion
from Persona import Persona
from logger_base import log

from cursor_del_pool import *

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
        with CursorDelPool() as cursor:
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
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Persona insertada: {persona}")
            # Devolvemos los valores insertados
            return cursor.rowcount



    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Persona actualizada: {persona}")
            # Devolvemos los valores insertados (cantidad)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Persona actualizada: {persona}")
            # Devolvemos los valores insertados (cantidad)
            return cursor.rowcount

if __name__ == "__main__":
    # Insertamos un objeto
    persona1 = Persona(nombre='Pedro', apellido='Garcia', email='pgarcia@hotmail.com')
    personas_insertadas = PersonaDao.insertar(persona1)
    log.debug(f"Personas insertadas: {personas_insertadas}")
    """
    # Eliminar un registro
    persona2= Persona(id_persona=2)
    persona_eliminada = PersonaDao.eliminar(persona2)
    log.debug(f"Personas Eliminada: {persona_eliminada}")
    """

    """
   # Actualizamos un registro
   persona2= Persona(2, "Prueba", "Prueba apellido", "pp@mail.com")
   personas_actualizadas = PersonaDao.actualizar(persona2)
   log.debug(f"Personas actualizadas: {personas_actualizadas}")
    """

"""
    #Seleccionar objeto
    personas = PersonaDao.seleccionar()
    for persona in personas:
        log.debug(persona)
"""



