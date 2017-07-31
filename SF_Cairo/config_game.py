import subprocess

external_constants = []
switches = ""
input = raw_input("Should the game terminate after certain duration? (y/n) \n")
if(input == "y"):
    external_constants.append("GAME_DURATION_TERMINAL")
    input = raw_input("Game duration (int):\n")
    external_constants.append("GAME_DURATION "+input)
    input = raw_input("Score after game duration has ended (int):\n")
    external_constants.append("GAME_OVER_SCORE "+input)


input = raw_input("Reward for hitting fortress with missile (int): \n")
external_constants.append("FORTRESS_SHOT_SCORE "+input)

input = raw_input("Penalty for being hit by fortress missile (negative int): \n")
external_constants.append("SHOT_BY_FORTRESS_PENALTY "+input)

input = raw_input("Amount of lives of the ship (int): \n")
external_constants.append("MAX_SHIP_DAMAGE "+input)

input = raw_input("Amount of lives of the fortress (int): \n")
input = str(int(input)-1)
external_constants.append("FORTRESS_LIVES "+input)

input = raw_input("Penalize wrapping? (y/n): \n")
if(input == "y"):
    external_constants.append("PENALIZE_WRAPPING")
    input = raw_input("Penalty for wrapping (negative int):\n")
    external_constants.append("PENALTY_WRAPPING "+input)
print(external_constants)
print("Switches: \n")
input = raw_input("GUI_INTERFACE (y/n): \n")
if(input == "y"):
    switches+=("-D GUI_INTERFACE ")

input = raw_input("GRID_MOVEMENT (y/n): \n")
if(input == "y"):
    switches+=("-D GRID_MOVEMENT ")

input = raw_input("NO_WRAP (y/n): \n")
if(input == "y"):
    switches+=("-D NO_WRAP ")

input = raw_input("NO_DIRECTION (y/n): \n")
if(input == "y"):
    switches+=("-D NO_DIRECTION ")

input = raw_input("DEBUG (y/n): \n")
if(input == "y"):
    switches+=("-D DEBUG ")

input = raw_input("NO_RANDOM_SPAWN (y/n): \n")
if(input == "y"):
    switches+=("-D NO_RANDOM_SPAWN ")

print(switches)

target = open('external_constants.h', 'w')
target.truncate()
target.write('#ifndef EXTERNAL_CONSTANTS\n#define EXTERNAL_CONSTANTS\n')
[target.write("#define "+constant+"\n") for constant in external_constants]
target.write('#endif')
target.close()

target = open('compile_game.sh', 'w')
target.truncate()
target.write('#!/bin/sh\nSwitches="'+switches+'"\n' )
target.write('eval "$(cat DE_Minimal.c | grep -m 4 "\-\-cflags cairo")"; cp *.so ../gym-master/gym/envs/space_fortress/linux2')
target.close()
