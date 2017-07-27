class Config:

    #Game envs are AIM, SFC and SFS
    GAME_ENV = 'SFC-v0'

    SO_FILES_PATH = '/home/pitur/Downloads/Gym-rijnder/gym-master/gym/envs/space_fortress/linux2'

    DEBUG_MODE = False

    # Game modes. Possible modes are 'rgb_array', 'human', 'human_sleep', 'minimal', 'minimal_sleep', 'minimal_debug', 'human_debug'

    MODE = 'minimal_debug'

    RENDER = False

    SAVE_IMAGES = False

    IMAGES_PATH = '/home/pitur/Pictures/SFS_snapshots/'

    GUI_INTERFACE = False

    #########################################################################
    # Game settings

    GUI_INTERFACE = False

    # TERMINAL STATES:
    # For aiming task: target_missed, game_duration, max_score
    # For control task: target_missed, game_duration, max_score
    # For sfs: no_lives_left, game_duration, max_score, ship_destroyed,

    TERMINAL_STATES = ['target_missed', 'game_duration', 'max_score']
    # Game settings for the aiming task

    GAME_DURATION = 2400

    # Game settings for the control task

    SWITCHES = ['GRID_MOVEMENT', 'NO_WRAP']

    MISSED_MINE_PENALTY = 0

    COLLECTED_MINE_REWARD = 1

    # Game settings for the simplified space fortress task

    LIVES = 3

    FORTRESS_HEALTH = 3
