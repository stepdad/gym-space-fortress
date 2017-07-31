class Config:

    #Game envs are AIM, SFC and SFS
    GAME_ENV = 'AIM-v0'


    DEBUG_MODE = False

    # Game modes. Possible modes are 'rgb_array', 'human', 'human_sleep', 'minimal', 'minimal_sleep', 'minimal_debug', 'human_debug'

    MODE = 'human_sleep'

    # Render the game?
    PLAY = True

    FRAME_SKIP = 1

    # if mode contains sleep

    SLEEP = 42

    DEBUG = False

    SAVE_IMAGES = False

    IMAGES_PATH = '/home/putri/Documents/Gym-rijnder/gym-master/gym/envs/space_fortress/snapshots'
