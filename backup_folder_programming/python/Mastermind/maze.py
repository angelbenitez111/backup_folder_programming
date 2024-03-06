import os
import random
import readchar

GAME_OVER_MESSAGE = "Game over"
POS_X = 0
POS_Y = 1
NUM_OF_MAP_OBJECTS = 11

obstacle_definition = """\
############################
                        ####
#####################   ####
#####################   ####
#############               
####################  ######
###############           ##
######               #######
############                
####   ##############      #
######                   ###
###### ##############       
####    ###############  ###
############################\
"""

end_game = False
died = False
crashed = False

my_position = [3, 1]
tail_legth = 0
blanks = 0
tail = []

map_objects = []

# create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

for y_axis in range(len(obstacle_definition)):

    for space_map in obstacle_definition[y_axis]:

        if space_map == " ":
            blanks += 1
# Main Loop
while not end_game:
    os.system("cls")
    # Generate random objects on the map
    while len(map_objects) < NUM_OF_MAP_OBJECTS:

        if blanks > ((len(tail) + 1) + NUM_OF_MAP_OBJECTS):
            new_position = [random.choice(range(MAP_WIDTH)), random.choice(range(MAP_HEIGHT))]

            if new_position != my_position and new_position not in map_objects and new_position not in tail\
                    and obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
                map_objects.append(new_position)

        else:
            break
    # Draw Map
    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for cordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None
            obstacle_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == cordinate_x and map_object[POS_Y] == cordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tail_piece in tail:

                if cordinate_x == tail_piece[POS_X] and cordinate_y == tail_piece[POS_Y]:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece

            if (obstacle_definition[cordinate_y][cordinate_x]) == "#":
                char_to_draw = "#"
                obstacle_in_cell = True

            if cordinate_x == my_position[POS_X] and cordinate_y == my_position[POS_Y]:
                char_to_draw = "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_legth += 1

                if tail_in_cell:
                    char_to_draw = "X"
                    end_game = True
                    died = True

                if obstacle_in_cell:
                    char_to_draw = "X"
                    end_game = True
                    crashed = True

            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    if died:
        print(GAME_OVER_MESSAGE)

    if crashed:
        print("You creshed through a wall")

    direction = readchar.readchar().decode()

    if direction == "W" or direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_legth]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "S" or direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_legth]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "A" or direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_legth]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "D" or direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_legth]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "Q" or direction == "q":
        end_game = True
