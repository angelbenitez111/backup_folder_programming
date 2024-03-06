import os
import readchar
import random

GAME_OVER_MESSAGE = "Game over"
POS_X = 0
POS_Y = 1
# 13 * 9
obstacle_definition = """\
###          
###          
###  ########
     ########
             
###          
###          
###  ########
###  ########\
"""

end_game = False
start_the_fight = False
index_pokemon = None

my_position = [5, 1]
# date of the combat
length_life_bar = 10

MY_POKEMON_NAME = ["Chamander"]
MY_POKEMON_LIFE = [80]
NAME_MY_POKEMON_ATTACK = [["Mar de llamas"]]
DAMAGE_MY_POKEMON_ATTACK = [[66]]

pokemon_trainers = [[11, 1], [1, 3]]

# 1| squirtle [1][n] 2| pikachu [2][n]
POKEMON_NAME = ["Squirtle", "Pikachu"]
LIFE_OF_POKEMONS = [80, 70]
DAMAGE_POKEMONS_ATTACK = [[10, 12, 9], [10, 11]]
NAME_POKEMONS_ATACK = [["Placaje", "Pistol water", "Bubble"], ["Bola voltio", "Onda trueno"]]

# create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# Main Loop
while not end_game:
    os.system("cls")
    # Draw Map
    print("+" + "-" * (MAP_WIDTH * 2) + "+")

    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for cordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            trainer_in_cell = False

            for pokemon_trainer in pokemon_trainers:
                if cordinate_x == pokemon_trainer[POS_X] and cordinate_y == pokemon_trainer[POS_Y]:
                    char_to_draw = "*"
                    trainer_in_cell = True

            if "#" == (obstacle_definition[cordinate_y][cordinate_x]):
                char_to_draw = "#"

            if cordinate_x == my_position[POS_X] and cordinate_y == my_position[POS_Y]:
                char_to_draw = "@"

                if trainer_in_cell:
                    start_the_fight = True
                    index_pokemon = int(pokemon_trainers.index([cordinate_x, cordinate_y]))
                    end_game = True

            print(" {}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * (MAP_WIDTH * 2) + "+")

    if not start_the_fight:

        direction = readchar.readchar().decode()
        new_position = None

        if direction == "W" or direction == "w":
            new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

        elif direction == "S" or direction == "s":
            new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

        elif direction == "A" or direction == "a":
            new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

        elif direction == "D" or direction == "d":
            new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

        elif direction == "Q" or direction == "q":
            end_game = True

        if new_position:
            if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
                my_position = new_position

if start_the_fight:

    INITIAL_MYPOKEMON_LIFE = MY_POKEMON_LIFE[0]
    INITIAL_POKEMON1_LIFE = LIFE_OF_POKEMONS[index_pokemon]

    mypokemon_life = INITIAL_MYPOKEMON_LIFE
    pokemon1_life = INITIAL_POKEMON1_LIFE

    turn = 1

    number_of_attacks_mypokemon = len(DAMAGE_MY_POKEMON_ATTACK[0])
    number_of_attacks_pokemon1 = len(DAMAGE_POKEMONS_ATTACK[index_pokemon])

    mypokemon_attack = None
    pokemon1_attack = None
    while mypokemon_life > 0 and pokemon1_life > 0:
        # Turn of my pokemon
        if turn == 1:

            while mypokemon_attack not in list(range(1, (number_of_attacks_mypokemon + 2))):
                os.system("cls")
                print("Turn of {}"
                      "\nWhat attack do you want to do:".format(MY_POKEMON_NAME[0]))

                for amount_options in range(number_of_attacks_mypokemon):
                    print("{}- {}".format(amount_options + 1, NAME_MY_POKEMON_ATTACK[0][amount_options]))

                print("{}- Do nothing".format(number_of_attacks_mypokemon + 1))

                try:
                    mypokemon_attack = int(input("Response: "))

                except ValueError:
                    input("Response invalid...")

            if mypokemon_attack in list(range(1, (number_of_attacks_mypokemon + 1))):
                pokemon1_life -= DAMAGE_MY_POKEMON_ATTACK[0][mypokemon_attack - 1]
                print("Has launched a/an {}".format(NAME_MY_POKEMON_ATTACK[0][mypokemon_attack - 1]))
            else:
                print("{} does nothing".format(MY_POKEMON_NAME[0]))

            if mypokemon_life < 0:  # prevent it from being a negative a value
                mypokemon_life = 0

            if pokemon1_life < 0:
                pokemon1_life = 0

            mypokemon_bar_life = int(mypokemon_life * length_life_bar / INITIAL_MYPOKEMON_LIFE)

            print("{} \n[{}{}] ({}/{})".format(MY_POKEMON_NAME[0], "#" * mypokemon_bar_life,
                                               " " * (length_life_bar - mypokemon_bar_life),
                                               INITIAL_MYPOKEMON_LIFE, mypokemon_life))

            pokemon1_bar_life = int(pokemon1_life * length_life_bar / INITIAL_POKEMON1_LIFE)

            print("{} \n[{}{}] ({}/{})".format(POKEMON_NAME[index_pokemon], "#" * pokemon1_bar_life,
                                               " " * int(length_life_bar - pokemon1_bar_life),
                                               INITIAL_POKEMON1_LIFE, pokemon1_life))

            turn = 0
            mypokemon_attack = None

            if pokemon1_life > 0 and mypokemon_life > 0:
                input("Enter to continue...")

        elif turn == 0:  # Turn of pikachu
            os.system("cls")

            print("\n" + "Turn for {}".format(POKEMON_NAME[index_pokemon]))

            pokemon1_attack = random.randint(1, len(DAMAGE_POKEMONS_ATTACK[index_pokemon]) + 1)

            if pokemon1_attack in list(range(1, (number_of_attacks_pokemon1 + 1))):
                mypokemon_life -= DAMAGE_POKEMONS_ATTACK[index_pokemon][pokemon1_attack - 1]
                print("Has launched a/an {}".format(NAME_POKEMONS_ATACK[index_pokemon][pokemon1_attack - 1]))

            else:
                print("{} does nothing".format(POKEMON_NAME[index_pokemon]))

            if mypokemon_life < 0:  # prevent it from being a negative a value
                mypokemon_life = 0

            if pokemon1_life < 0:
                pokemon1_life = 0

            mypokemon_bar_life = int(mypokemon_life * length_life_bar / INITIAL_MYPOKEMON_LIFE)
            print("{} \n[{}{}] ({}/{})".format(MY_POKEMON_NAME[0], "#" * mypokemon_bar_life,
                                               " " * (length_life_bar - mypokemon_bar_life),
                                               INITIAL_POKEMON1_LIFE, mypokemon_life))

            pokemon1_bar_life = int(pokemon1_life * length_life_bar / INITIAL_POKEMON1_LIFE)
            print("{} \n[{}{}] ({}/{})".format(POKEMON_NAME[index_pokemon], "#" * pokemon1_bar_life,
                                               " " * int(length_life_bar - pokemon1_bar_life),
                                               INITIAL_POKEMON1_LIFE, pokemon1_life))

            turn = 1
            pikachu_attack = None

            if pokemon1_life > 0 and mypokemon_life > 0:
                input("Enter to continue...")

    if mypokemon_life <= 0:
        print("\nwin for {}".format(MY_POKEMON_NAME[0]))

    elif pokemon1_life <= 0:
        print("\nWin for {}".format(POKEMON_NAME[index_pokemon]))

    input("Enter to finalize...")
