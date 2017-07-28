# -*- coding: utf-8 -*-

#!/usr/bin/env python
import gym
import sys
import numpy as np
from random import random
import cv2 # remove at one point
from time import sleep
from Config import Config

try:
	from pynput.keyboard import Key, Listener
except:
	print("You don't seem to have 'pynput' installed 😕 . Install it with 'pip install pynput'. \n")
	exit(0)



def on_press(key):
	#		LEFT = 0
	#		UP = 1
	#		RIGHT = 2
	#		SHOOT = 3
	global current_key

	key_to_action = {Key.left : 0, Key.up : 1, Key.right : 2, Key.space : 3, Key.down : 3}

	if key in key_to_action.keys():
		current_key = key_to_action[key]
	else:
		current_key = 4


def on_release(key):
	pass

def on_release(key):
	pass

current_key = 1
if Config.MODE.endswith("debug"):
	print("Note that this script should be run as super user under OS X 👁")


env = gym.make(Config.GAME_ENV)



with Listener(on_press=on_press, on_release=on_release) as listener:
	for game in range(5):
		env.reset()
		for t in range(250000):
			env.render()
#			if render_mode.endswith('debug'):
			action = current_key
#			else:
#				action = env.action_space.sample()


			# Uncomment this for perfect play 👌
	#           ==============================
	#			if 0.7 < random():
	#				action = env.best_action()
	#			else:
	#				env.best_waction()
	#			==============================

			observation, reward, done, _ = env.step(action)
			print(reward)

			if done:
				print("terminal")
				break
	#			print("Done!")
	#			count += 1
				# print("Episode finished after {} timesteps".format(t+1))
	#				break
