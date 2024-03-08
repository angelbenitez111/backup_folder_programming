from logger_base import log


class Persona:
    # El valor por defecto es None
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'\n\n**Datos del objeto Persona**\n- Id_persona: {self._id_persona}\n- Nombre: {self._nombre}\n- Apellido: {self._apellido}\n- Email: {self._email}'

    # Metodos GET
    @property
    def id_persona(self):
        return self._id_persona

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def email(self):
        return self._email

    # Metodos SET
    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @email.setter
    def email(self, email):
        self._email = email




if __name__ == "__main__":
    persona1 = Persona(1, 'Juan', 'Perez', 'jperez@mail.com')
    log.debug(persona1)
    # Simular un insert
    persona1 = Persona(nombre='Juan', apellido='Perez', email='jperez@mail.com')
    log.debug(persona1)
    # Simular un delete
    persona1 = Persona(id_persona=1)
    log.debug(persona1)