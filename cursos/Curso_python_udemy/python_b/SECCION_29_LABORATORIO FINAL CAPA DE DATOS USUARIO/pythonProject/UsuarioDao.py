from Usuario import Usuario
from logger_base import log
from Conexion import Conexion

from CursorDelPool import CursorDelPool

class UsuarioDao:
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%'
    @classmethod
    def seleccionar(cls):
        # With this structure we automated the open and closed of the cursor
        with CursorDelPool() as cursor:
            # Execute the sentence SQL
            cursor.execute(cls._SELECCIONAR)
            # We save the register
            registros = cursor.fetchall()

            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            # The function receive a tuple
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario insertado: {usuario}')
            # Return the number of rows affected
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool as cursor:
            valores = (usuario.id_usuario)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Usuario eliminado: {usuario}')
            return cursor.rowcount

if __name__ == "__main__":
#    usuario1 = Usuario(id_usuario=None, username= 'Jennifer_mi_amor', password= 'Claudio')
#    usuarios_insertados = UsuarioDao.insertar(usuario1)
#    log.debug(f'usuarios insertados: {usuarios_insertados}')

    usuario2 = Usuario(id_usuario=3, username='Jennifer_mi_amor', password='angelito el mas bonito')
    usuario_actualizado = UsuarioDao.actualizar(usuario2)




