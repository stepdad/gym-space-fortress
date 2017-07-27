cd SF_Control$Switches="-D GRID_MOVEMENT -D NO_WRAP "
eval "$(cat DE_Minimal.c | grep -m 4 "\-\-cflags cairo")"; cp *.so /home/pitur/Downloads/Gym-rijnder/gym-master/gym/envs/space_fortress/linux2