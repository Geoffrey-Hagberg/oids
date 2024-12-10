import pygame
pygame.font.init()

SCREEN_WIDTH = 1520
SCREEN_HEIGHT = 960

ASTEROID_SCALAR = 15
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.5  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_SCALAR * ASTEROID_KINDS

BIOME_THRESHOLD = 2500

PLAYER_RADIUS = 15
PLAYER_TURN_SPEED = 240
PLAYER_SPEED = 200
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.4

SHIELD_RADIUS = PLAYER_RADIUS * 2
SHIELD_FULL_CHARGE = 600
SHIELD_RECHARGE_RATE = SHIELD_FULL_CHARGE / 2400
SHIELD_RECHARGE_SCALAR = 6
SHIELD_ACTIVE_COLOR = (140, 220, 255)
SHIELD_INACTIVE_COLOR = (105, 10, 15)
SHIELD_CHARGE_POSITION = (8, SCREEN_HEIGHT - 40)
SHIELD_CHARGE_DIMENSIONS = (SCREEN_WIDTH / 4, 24)
SHIELD_CHARGE_RATE_COLOR = SHIELD_ACTIVE_COLOR

SHOT_RADIUS = 3

SCORE_SCALAR = 30
SCORE_DIMENSIONS = (SCREEN_WIDTH, 120)
SCORE_POSITION = (8, 0)
SCORE_FONT = pygame.font.SysFont("helveticaneue", 48)
SCORE_PATH = "./local/high_score.txt"