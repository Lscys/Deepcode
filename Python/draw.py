import os
import readchar
import random

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGTH = 15
NUM_OF_MAP_OBJECTS = 11

obstacle_definition = """\
##########################
                       ####
####################   ####
####################   ####
###########
###################  ######
###############         ##
#######            ########
##############
######################   ###
#####     ########         #
########                 ###
######## #########
#####    ###########    ####
############################\
"""

# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

# Draw map
print("+" + "-" * MAP_WIDTH * 3 + "+")

for coordinate_y in range(MAP_HEIGTH):
        print("|", end="")

    
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None


        if obstacle_definition[coordinate_y][coordinate_x] == "#":
            char_to_draw = "#"

            print(" {} ".format(char_to_draw), end="")
        print("|")

print("+" + "-" * MAP_WIDTH * 3 + "+")


