from random import randint
import os

INITIAL_PIKACHU_LIFE = 80
INITIAL_SQUIRTLE_LIFE = 90

pikachu_life = INITIAL_PIKACHU_LIFE
squirtle_life = INITIAL_SQUIRTLE_LIFE

length_life_bar = 10
squirtle_attack = None
pikachu_attack = None
turn = 1

while pikachu_life > 0 and squirtle_life > 0:
    if turn == 1:  # Turn of squirt
        while squirtle_attack != 1 and squirtle_attack != 2 and squirtle_attack != 3 and squirtle_attack != 4:
            squirtle_attack = input("\nTurn of squirtle"
                                    "What attack do you want to do\n"
                                    "1- Placate\n"
                                    "2- Pistola de Agua\n"
                                    "3- Burbuja\n"
                                    "Attack: ")

            if squirtle_attack != '':
                squirtle_attack = int(squirtle_attack)

        if squirtle_attack == 1:
            pikachu_life -= 10
            print("\nHas launched a Placate")

        elif squirtle_attack == 2:
            pikachu_life -= 12
            print("\nHas launched a Placate")

        elif squirtle_attack == 3:
            pikachu_life -= 9
            print("\nHas launched a Placate")

        elif pikachu_attack == 4:
            print("squirtle does nothing")

        if squirtle_life < 0:  # prevent it from being a negative a value
            squirtle_life = 0

        if pikachu_life < 0:
            pikachu_life = 0

        squirtle_bar_life = int(squirtle_life * length_life_bar / INITIAL_SQUIRTLE_LIFE)
        print("Squirtle \n[{}{}] ({}/{})".format("#" * squirtle_bar_life, " " * (length_life_bar - squirtle_bar_life),
                                                 INITIAL_SQUIRTLE_LIFE, squirtle_life))

        pikachu_bar_life = int(pikachu_life * length_life_bar / INITIAL_PIKACHU_LIFE)
        print("Pikachu \n[{}{}] ({}/{})".format("#" * pikachu_bar_life, " " * int(length_life_bar - pikachu_bar_life),
                                                INITIAL_PIKACHU_LIFE, pikachu_life))

        turn = 0
        squirtle_attack = None

        if pikachu_life > 0 and squirtle_life > 0:
            input("Enter to continue...")
            os.system("cls")

    elif turn == 0:  # Turn of pikachu
        print("\n" + "Turn for pikachu")

        pikachu_attack = randint(1, 2)

        if pikachu_attack == 1:
            squirtle_life -= 10
            print("\nHas launched a Bola Voltio")

        elif pikachu_attack == 2:
            squirtle_life -= 11
            print("\nHas launched a onda trueno")


        if squirtle_life < 0:  # prevent it from being a negative a value
            squirtle_life = 0

        squirtle_bar_life = int(squirtle_life * length_life_bar / INITIAL_SQUIRTLE_LIFE)
        print("Squirtle \n[{}{}] ({}/{})".format("#" * squirtle_bar_life, " " * (length_life_bar - squirtle_bar_life),
                                                 INITIAL_SQUIRTLE_LIFE, squirtle_life))

        if pikachu_life < 0:  # prevent it from being a negative a value
            pikachu_life = 0

        pikachu_bar_life = int(pikachu_life * length_life_bar / INITIAL_PIKACHU_LIFE)
        print("Pikachu \n[{}{}] ({}/{})".format("#" * pikachu_bar_life, " " * int(length_life_bar - pikachu_bar_life),
                                                INITIAL_PIKACHU_LIFE, pikachu_life))

        turn = 1
        pikachu_attack = None

        if pikachu_life > 0 and squirtle_life > 0:
            input("Enter to continue...")
            os.system("cls")

if squirtle_life <= 0:
    print("\nwin for pikachu")

elif pikachu_life <= 0:
    print("\nWin for Sqrit")

input("Enter to finalize...")

