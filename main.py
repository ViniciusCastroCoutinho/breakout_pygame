import pygame

pygame.init()
# window config
HEIGHT = 850
WIDTH = 725

# Set the screen size and create a Pygame display
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BreakOut - PyGame Edition - 2023-11-30")

# game loop
game_loop = True
game_clock = pygame.time.Clock()
game_over = False

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')

# bricks
brick_size = ((WIDTH - 39) / 14, 10)
brick_list = [[[pygame.Rect(((WIDTH + 3) / 14 * j, 150 + i * 15), brick_size), 1] for j in range(14)]for i in range(8)]
for i in range(8):
    print(brick_list[i])
can_break = True
breakout = False
hits = 0

# player
player_move_left = False
player_move_right = False
player = pygame.Rect(WIDTH/2, HEIGHT - 80, 70, 10)
player_parts = player[2] / 8

# HUD
points = 0
lives = 3
black = (0, 0, 0)
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
font_lives = pygame.font.Font('assets/PixelGameFont.ttf', 20)
font_points = pygame.font.Font('assets/PixelGameFont.ttf', 32)

# walls
upper_wall = pygame.Rect(0, 0, WIDTH, 60)
left_wall = pygame.Rect(0, 0, 10, HEIGHT)
right_wall = pygame.Rect(WIDTH - 10, 0, 10, HEIGHT)


# ball config
ball_speed_x = -5
ball_speed_y = 4
ball = pygame.Rect(200, 350, 10, 10)


def ball_reset():
    global ball_speed_x, ball_speed_y, hits, can_break, player
    ball_speed_x = -5
    ball_speed_y = 4
    ball[0] = 200
    ball[1] = 400
    can_break = True
    player[2] = 70
    hits = 0


def ball_collision_angle():
    global player_parts, ball_speed_x
    for i in range(8):
        if player[0] + i * player_parts < ball[0] + 10 < player[0] + (i + 1) * player_parts:
            if i > 3:
                ball_speed_x = -(3 - i) * 2
            else:
                ball_speed_x = -(4 - i) * 2
        break


def visuals():
    screen.fill(black)
    # walls
    pygame.draw.rect(screen, (000, 90, 137), player)
    pygame.draw.rect(screen, (255, 255, 255), upper_wall)
    pygame.draw.rect(screen, (255, 255, 255), right_wall)
    pygame.draw.rect(screen, (255, 255, 255), left_wall)

    # bricks
    for i in range(8):
        if i < 2:
            for j in range(14):
                if brick_list[i][j][1]:
                    pygame.draw.rect(screen, (255, 0, 0), brick_list[i][j][0])