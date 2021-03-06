import pygame

margin = 2
WIDTH = 1000
HEIGHT = 720 + margin
screen = pygame.display.set_mode([WIDTH, HEIGHT])

BOARD_SIZE = 12
grid_size = int(round((HEIGHT - margin) / BOARD_SIZE))

FPS = 20
fpsClock = pygame.time.Clock()


BULLET_SIZE = 8
ENEMY_IMG_SIZE = grid_size // 2

HP_BAR_THICKNESS = 4
HP_BAR_ABOVE_ENEMY_CENTER = ENEMY_IMG_SIZE // 2 + 8
HP_BAR_BORDER = 1

tower_font_size = 14
slot_font_size = 14
path_dot_size = 28


ENEMY_SPAWN_INTERVAL = 800  # ms
FIRST_WAVE_DELAY = 30000
WAVE_DELAY = 15000


DEFEAT_ENEMY_SCORE = 10
WAVE_CLEAR_SCORE = 60
SCORE_MULTIPLIER_ADD = 0.25
INIT_ENEMY_NUM = 12
INIT_PORT_HP = 20
INIT_TOWER_TO_PLACE = 15
WAVE_CLEAR_TOWER_ADD = 7

SHOW_AIM_LINE = 1  # if 1, show aim line

TOWER_MAX_LVL = 4
# (atk, atk_range)
TOWER_ATTR_DICT = {
    'Cannon1': (35, round(grid_size * 3.1)),
    'Cannon2': (82, round(grid_size * 3.1)),
    'Cannon3': (193, round(grid_size * 3.6)),
    'Cannon4': (454, round(grid_size * 3.6)),

    'Sniper1': (70, round(grid_size * 5.1)),
    'Sniper2': (164, round(grid_size * 5.1)),
    'Sniper3': (377, round(grid_size * 6.1)),
    'Sniper4': (875, round(grid_size * 6.1)),

    'Crusher1': (18, round(grid_size * 2.1)),
    'Crusher2': (43, round(grid_size * 2.1)),
    'Crusher3': (108, round(grid_size * 2.1)),
    'Crusher4': (260, round(grid_size * 2.1))
}


#### FOR TESTING
# TOWER_ATTR_DICT = {
#     'Cannon1': (1, round(grid_size * 3.1)),
#     'Cannon2': (1, round(grid_size * 3.1)),
#     'Cannon3': (1, round(grid_size * 3.6)),
#     'Cannon4': (1, round(grid_size * 3.6)),
#
#     'Sniper1': (1, round(grid_size * 5.1)),
#     'Sniper2': (1, round(grid_size * 5.1)),
#     'Sniper3': (1, round(grid_size * 6.1)),
#     'Sniper4': (1, round(grid_size * 6.1)),
#
#     'Crusher1': (1, round(grid_size * 2.1)),
#     'Crusher2': (1, round(grid_size * 2.1)),
#     'Crusher3': (1, round(grid_size * 2.6)),
#     'Crusher4': (1, round(grid_size * 2.6))
# }

# (hp, ms)
ENEMY_ATTR_DICT = {
    'Circle': (170, 80 / FPS),
    'Square': (310, 50 / FPS),
    'Triangle': (112, 120 / FPS)
}
MAX_ENEMY_TYPE = len(ENEMY_ATTR_DICT)
MAX_ENEMY_NUM = 60

CIRCLE_COLOR = (152, 191, 100)
SQUARE_COLOR = (252, 106, 3)
TRIANGLE_COLOR = (255, 239, 0)

CANNON_ATK_INT = 1
SNIPER_ATK_INT = 2.5
CRUSHER_ATK_INT = 1.2
# Bullet Speed
CANNON_BS = 400 / FPS
SNIPER_BS = 800 / FPS


white = (255, 255, 255)
green = (0, 255, 0)
lighter_green = (0, 200, 0)
blue = (0, 0, 128)
azure = (170, 240, 250)
black = (0, 0, 0)
red = (255, 0, 0)
dark_grey = (43, 45, 47)
light_grey = (180, 180, 180)
indigo = (40, 30, 93)

ATK_RANGE_COLOR = (160, 220, 235)
AIMING_LINE_COLOR = (3, 192, 74)


