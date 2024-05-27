from UsuarioDao import UsuarioDao
from logger_base import log
from Usuario import Usuario
# We start the program
response = None
menu_inicio = """
Opciones:
1. Listar usuarios
2. Agregar usuario
3. Modificar usuario
4. Eliminar usuario
5. Salir
Escribe tu opción (1-5): """

log.basicConfig(level=log.INFO)

while response != 5:
    try:
        response = int(input(menu_inicio))
    except:
        log.info('Invalid')
        continue
    # List users
    if response == 1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)

    # Add user
    elif response == 2:
        username = str(input('Escribe el username: '))
        password = str(input('Escribe el password: '))

        usuario_a_insertar = Usuario(username=username, password=password)
        log.info(f'Usuarios insertados: {UsuarioDao.insertar(usuario_a_insertar)}')

    # Modify user
    elif response == 3:
        id_usuario = int(input('Escribe el id_usuario a modificar: '))
        username = str(input('Escribe el username: '))
        password = str(input('Escribe el password: '))

        usuario_a_actualizar = Usuario(id_usuario, username, password)
        log.info(f'Usuarios actualizados: {UsuarioDao.actualizar(usuario_a_actualizar)}')

    # Delete user
    elif response == 4:
        id_usuario = int(input('Escribe el id_usuario a eliminar: '))
        usuario_a_eliminar = Usuario(id_usuario=id_usuario)
        log.info(f'Usuarios eliminados: {UsuarioDao.eliminar(usuario_a_eliminar)}')

    elif response == 5:
            log.debug('Fin del programa...')
            break

    else:
        log.info('Invalid response')
