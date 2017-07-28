#!/bin/sh
Switches=""
eval "$(cat DE_Minimal.c | grep -m 4 "\-\-cflags cairo")"; cp *.so ../gym-master/gym/envs/space_fortress/linux2