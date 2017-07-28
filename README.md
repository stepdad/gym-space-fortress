# gym-space-fortress
*UNDER CONSTRUCTION*


This repository contains a gym environment for the Simplified Space Fortress game and its subtasks.

The three tasks contained in this repository are:

The Simplified Space Fortress game (SFS-v0)

The Control task (SFC-v0)

The Aiming task (AIM-v0)

A Gym environment can be created by compiling the desired game and configuring the environment. This will be demonstrated by means of an example.

*Game compilation*
To compile the Control task, navigate towards the folder that holds its c-code (SF_Control) and run the configuration/settings script config_game.py. After choosing the desired settings, run ./compile_game.sh. This copies the shared object files of the game to a location where they will be easily accessible for the Gym environment. The Control task is now compiled with the desired settings.
Advanced settings and parameters can be adjusted by changing values in external_constants.h or myconst.h. Run ./compile_game.sh after every adjustment in the game.

*Environment configuration*
Navigate to Gym-rijnder/gym-master/gym/envs/space_fortress/ and change the desired values in Config.py. To check whether the game works as desired, execute run.py.

When the game and environment are configured as desired, the environment can be created by calling gym.make(SFC-v0) (or gym.make(SFS-v0), gym.make(AIM-v0)).
**
