# gym-space-fortress



This repository contains a gym environment for the Simplified Space Fortress game and its subtasks.

The three tasks contained in this repository are:

The Simplified Space Fortress game (SFS-v0)

The Control task (SFC-v0)

The Aiming task (AIM-v0)

*Installation*
To install the current gym framework, navigate to Gym-rijnder/gym-master and execute:

pip install -e .

Installation should now be complete.


A Gym environment can be created by compiling the desired game and configuring the environment. This will be demonstrated by means of an example.

*Game compilation*

To compile the Control task, navigate towards the folder that holds its c-code (SF_Control) and run the configuration/settings script config_game.py. After choosing the desired settings, run ./compile_game.sh. This copies the shared object files of the game to a location where they will be easily accessible for the Gym environment. The Control task is now compiled with the desired settings.

For AIM, navigate to /AIM_Cairo and for SFS navigate to /SF_Cairo.

Advanced settings and parameters can be adjusted by changing values in external_constants.h or myconst.h. When applying custom changes, compile the game manually:

Navigate to (/SF_Control or /AIM_Cairo or /SF_Cairo). Define the desired switches by setting the shell variable Switches to the desired switches e.g.:

Switches="-D NO_WRAP -D GRID_MOVEMENT -D GUI_INTERFACE"

then run:

eval "$(cat DE_Minimal.c | grep -m 4 "\-\-cflags cairo")"; cp *.so ../gym-master/gym/envs/space_fortress/linux2

The game is now compiled with custom settings.

*Environment configuration*

Navigate to Gym-rijnder/gym-master/gym/envs/space_fortress/ and change the desired values in Config.py. To check whether the game works as desired, execute run.py.

When the game and environment are configured as desired, the environment can be created by calling gym.make(SFC-v0) (or gym.make(SFS-v0), gym.make(AIM-v0)).
**
