from Config import Config
import subprocess

path = ''
if Config.GAME_ENV == 'AIM-v0':
	path = 'AIM_Cairo'
elif Config.GAME_ENV == 'SFC-v0':
	path = 'SF_Control'
	target = open(path+'/external_constants.h', 'w')
	target.truncate()
	target.write('#ifndef EXTERNAL_CONSTANTS')
	target.write('\n')
	target.write('#define EXTERNAL_CONSTANTS')
	target.write('\n')
	target.write('#define GAME_DURATION '+str(Config.GAME_DURATION))
	target.write('\n')
	target.write('#define MISSED_MINE_PENALTY '+str(Config.MISSED_MINE_PENALTY))
	target.write('\n')
	target.write('#define COLLECTED_MINE_REWARD '+str(Config.COLLECTED_MINE_REWARD))
	target.write('\n')
	if 'game_duration' in Config.TERMINAL_STATES:
		target.write('#define GAME_DURATION_TERMINAL 1')
	else:
		target.write('#define GAME_DURATION_TERMINAL 0')
	target.write('\n')
	target.write('#endif')
	target.close()
else:
	path = 'SF_Cairo-v0'

switches = ''
switches = ['-D '+switch+' ' for switch in Config.SWITCHES]
switches = ''.join(switches)
bash_script = open(path+'/compile_game.sh', 'w')
bash_script.truncate()
bash_script.write('#!/bin/sh')
bash_script.write('\n')
bash_script.write('Switches="'+switches+'"')
bash_script.write('\n')
bash_script.write('eval "$(cat DE_Minimal.c | grep -m 4 "\-\-cflags cairo")"; cp *.so '+Config.SO_FILES_PATH)
bash_script.close()
subprocess.call(['chmod', 'a+x', path+'/compile_game.sh'])
# subprocess.Popen('./'+path+'/compile_game.sh', cwd=path)
subprocess.call('echo YOO', shell=True)
# subprocess.call('./'+path+'/compile_game.sh')