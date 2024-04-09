import logging as log

# DEBUG, INFO --> WARNING, ERROR CRITICAL
# https://docs.python.org/3/howto/logging.html
log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s ',
                datefmt='%I:%M:%S %p',
                # date format | I = hora | M= minutos | %S segundos | %p PM o AM
                handlers=[
                    # configurar el lugar del archivo
                    log.FileHandler('Log/lab_usuarios.log'),
                    # Agregamos informacion a un archivo (de la consola)
                    log.StreamHandler()
                    # Agregamos informacion al stream handler (la consola)
                ])

<<<<<<< HEAD
log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s]',
                datefmt='%I:%M:%S %p',
                # date format | I = hora | M= minutos | %S segundos | %p PM o AM
                handlers=[
                    # configurar el lugar del archivo
                    log.FileHandler('Log/lab_usuarios.log'),
                    # Agregamos informacion a un archivo (de la consola)
                    log.StreamHandler()
                    # Agregamos informacion al stream handler (la consola)
                ])
=======
>>>>>>> 9e5e5bf217facc97ba41904bc40aa07a0b82af10
"""
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])
"""
# Handler = un recurso a donde vamos a mandar informacion
# %(asctime)s = agrega el tiempo (fecha y hora) al mensaje de log
# %s(levelname)s = nivel del mensaje que estamos mandando a consola
# [%(filename)s] = agrega el nombre del archivo al mensaje del log
# %(lineno)s = agrega el número de linea al mensaje del log
# %(message)s = Esto muestra el mensaje que hemos agregado al log


if __name__ == '__main__':
<<<<<<< HEAD
    log.info('Prueba de mensaje')
=======

>>>>>>> 9e5e5bf217facc97ba41904bc40aa07a0b82af10
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')

