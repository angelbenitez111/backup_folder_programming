PicachuVida=100
chamanderVida=100
PicachuAtaque=50
chamanderAtaque=45
picachu=45
turno= 1

while PicachuVida and chamanderVida > 0:
    if turno == 1:
        chamanderVida= chamanderVida - PicachuAtaque
        turno=0
    else:
        PicachuVida= PicachuVida - chamanderAtaque
        turno=1
else:
    if PicachuVida <= 0:
        print("Gana chamander")
    else:
        print("gana picachu")
"""Esta partida esta totalmente arreglada"""