from logger_base import log

class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    def __str__(self):
        return f'Id Usuario: {self._id_usuario}, Username: {self._username}, Password: {self. _password}'


    # Metodos get
    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    # Metodos set
    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @username.setter
    def username(self, username):
        self._username = username

    @password.setter
    def password(self, password):
        self._password = password


if __name__ == '__main__':
    usuario1 = Usuario(1, 'Pepito', )
    log.debug(usuario1)
