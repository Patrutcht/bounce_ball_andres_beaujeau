import csv
import numpy as np
import pygame
from assets import button
from game import Game
import time

# lien utile https://www.youtube.com/watch?v=2iyx8_elcYg
WIDTH = 1200
HEIGHT = 600
BOARD_WIDTH = 550
BOARD_HEIGHT = 550
COORDS = [(900, 150), (900, 400)]

pygame.init()
pygame.display.set_caption("Bounce Box")
icon = pygame.image.load('assets/image/icon.png')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.flip()
running = True
clock = pygame.time.Clock()


def angle(p1: pygame.Vector2, p2: pygame.Vector2):
    """
    Calculate the angle formed by a segment
    :param p1: pygame.Vector2
    :param p2: pygame.Vector2
    :return: float
    """
    distance = pygame.Vector2.distance_to(p1, p2)
    if distance == 0:
        return 0

    delta_y = p1.y - p2.y
    delta_x = p1.x - p2.x

    sin_component = delta_y / distance
    cos_component = delta_x / distance
    return np.sign(np.arcsin(sin_component)) * np.arccos(cos_component)


def draw_objects(surface: pygame.Surface, objects):
    """
    Draw the objects on the screen
    :param surface: pygame.Surface screen to draw in
    :param objects: list objects to draw
    """

    for obj in objects:
        obj.draw(surface)
    pygame.display.flip()


fonts = pygame.font.get_fonts()
text_font = pygame.font.SysFont(fonts[1], 18)
name_font = pygame.font.SysFont(fonts[1], 80)


def draw_text(text, font, text_col, coord):
    """
    Draw a text on the pygame window
    :param text: str text to display
    :param font: pygame.Font to write in
    :param text_col: pygame.Color color of the text
    :param coord: tuple coordinates of the text
    """

    img = font.render(text, True, text_col)
    screen.blit(img, coord)

player2ai = False
menu = True
start = False
Player1 = False
Player2 = False
play_game = False
played_turn = False
wait = False
p1_name = ""
p2_name = ""
player = None
max_dist = 90
radius = 10
c = 0.35
dt = 1 / 60
score = [0, 0]
title = pygame.image.load('assets/image/title.png')
space = pygame.image.load('assets/image/space.png')
winner_screen = pygame.image.load('assets/image/winner.png')
p1 = pygame.image.load('assets/image/player1.png')
p2 = pygame.image.load('assets/image/player2.png')
player1_img = pygame.image.load('assets/image/P1_t.png')
player1_img = pygame.transform.scale(player1_img, (94, 84))
player2_img = pygame.image.load('assets/image/P2_t.png')
player2_img = pygame.transform.scale(player2_img, (94, 84))
winner = False

play_img = pygame.image.load('assets/image/play.png').convert_alpha()
play_img = pygame.transform.scale(play_img, (300, 90))
start_img = pygame.image.load('assets/image/start.png').convert_alpha()
start_img = pygame.transform.scale(start_img, (300, 97))
next_img = pygame.image.load('assets/image/next.png').convert_alpha()
next_img = pygame.transform.scale(next_img, (300, 90))
bot_img = pygame.image.load('assets/image/bot.png').convert_alpha()

bot_img = pygame.transform.scale(bot_img, (300, 90))

# create button instances
play_button = button.Button(450, 250, play_img, 1)
start_button = button.Button(450, 350, start_img, 1)
next_button = button.Button(750, 350, next_img, 1)
bot_button = button.Button(450, 470, bot_img, 1)

while running:
    for i in pygame.event.get():
        if i.type == pygame.TEXTINPUT and Player1:
            p1_name += i.text
        if i.type == pygame.KEYDOWN and Player1:
            if i.key == pygame.K_BACKSPACE:
                p1_name = p1_name[:-1]
        if i.type == pygame.TEXTINPUT and Player2:
            p2_name += i.text
        if i.type == pygame.KEYDOWN and Player2:
            if i.key == pygame.K_BACKSPACE:
                p2_name = p2_name[:-1]
        if i.type == pygame.MOUSEBUTTONDOWN and not played_turn and start:
            played_turn = True
            balls = bounce_box.board.get_balls()
            mouse_coord = pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            white_coord = bounce_box.board.get_balls()[0].get_pos()
            dist = pygame.Vector2.distance_to(mouse_coord, white_coord)
            white_ball = balls[0]
            white_ball.set_player(player)
            if dist < max_dist:
                white_ball.set_speed(c * (mouse_coord[0] - white_coord[0]), c * (mouse_coord[1] - white_coord[1]))
            else:
                direction = pygame.Vector2.normalize(mouse_coord - white_coord)
                speed = direction * max_dist
                white_ball.set_speed(c * speed[0], c * speed[1])
            bounce_box.board.set_balls([white_ball] + balls[1:])
            played_turn = True
        if i.type == pygame.KEYDOWN and wait:
            if i.key == pygame.K_SPACE:
                start = True
                wait = False
        if i.type == pygame.QUIT:
            running = False
            break
    if menu:
        screen.fill(pygame.Color(10, 150, 10))
        screen.blit(title, (320, 100))
        if play_button.draw(screen):
            Player1 = True
            menu = False
    if Player1:
        screen.fill(pygame.Color(10, 150, 10))
        screen.blit(p1, (380, 100))
        draw_text("(choose a name)", text_font, pygame.Color(0, 0, 0), (510, 180))
        draw_text(p1_name, name_font, pygame.Color(210, 210, 210), (300, 200))
        if next_button.draw(screen):
            Player1 = False
            Player2 = True
    if Player2:
        screen.fill(pygame.Color(10, 150, 10))
        screen.blit(p2, (380, 100))
        draw_text("(choose a name)", text_font, pygame.Color(0, 0, 0), (510, 180))
        draw_text(p2_name, name_font, pygame.Color(210, 210, 210), (300, 200))
        if start_button.draw(screen):
            Player2 = False
            wait = True
        if bot_button.draw(screen):
            Player2= False
            wait = True
            player2ai=True
            p2_name="BOT"
    if wait:
        screen.fill(pygame.Color(180, 180,180))
        screen.blit(space, (124, 250))

    if start:
        screen.fill(pygame.Color(220, 220, 220))
        if not play_game:

            bounce_box = Game([[p1_name,False], [p2_name,player2ai]], 6, BOARD_WIDTH, BOARD_HEIGHT)
            player = bounce_box.get_players()[0]
            play_game = True

        elif not bounce_box.board.check_move() and not played_turn:
            if player.bot:
                whiteball = bounce_box.board.get_balls()[0]
                whiteball.set_player(player)
                direction=bounce_box.board.nearest_ball(whiteball)
                whiteball.set_speed(c*max_dist*direction.x,c*max_dist*direction.y)
                played_turn=True
            else:
                bounce_box.draw(screen, text_font)
                screen.blit(player1_img, (900, 30))
                screen.blit(player2_img, (900, 280))
                mouse_coord = pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                white_coord = bounce_box.get_board().get_balls()[0].get_pos()
                phi = angle(mouse_coord, white_coord)
                dist = pygame.Vector2.distance_to(mouse_coord, white_coord)
                if dist < max_dist:
                    pygame.draw.polygon(screen, pygame.Color(185, 122, 87, 10), [mouse_coord, (
                        white_coord.x + radius * np.sin(phi), white_coord.y - radius * np.cos(phi)), (
                                                                                  white_coord.x - radius * np.sin(phi),
                                                                                  white_coord.y + radius * np.cos(
                                                                                      phi))])

                else:
                    pygame.draw.polygon(screen, pygame.Color(185, 122, 87, 120),
                                    [(white_coord[0] + max_dist * np.cos(phi), white_coord[1] + max_dist * np.sin(phi)),
                                     (white_coord.x + radius * np.sin(phi),
                                      white_coord.y - radius * np.cos(phi)), (
                                         white_coord.x - radius * np.sin(phi),
                                         white_coord.y + radius * np.cos(
                                             phi))])


        elif bounce_box.board.check_move() and played_turn:
            bounce_box.draw(screen, text_font)
            screen.blit(player1_img, (900, 30))
            screen.blit(player2_img, (900, 280))
            bounce_box.board.step(dt)
            ind = bounce_box.get_players().index(player)
            score[ind] = bounce_box.get_players()[ind].get_score()
        elif not bounce_box.board.check_move() and played_turn:
            bounce_box.draw(screen, text_font)
            screen.blit(player1_img, (900, 30))
            screen.blit(player2_img, (900, 280))
            player = bounce_box.get_players()[abs(bounce_box.get_players().index(player) - 1)]
            played_turn = False
    if max(score) == 6:
        start = False
        ind = score.index(6)
        screen.fill(pygame.Color(180, 180,180))
        if ind == 0:
            screen.blit(p1, (380, 250))
            winner = p1_name
        else:
            screen.blit(p2, (380, 250))
            winner = p2_name
        screen.blit(winner_screen, (360, 150))



    pygame.display.flip()

if winner:
    with open('assets/game_stats.csv', 'a', newline='') as f:
        stats = csv.writer(f, delimiter=';')
        stats.writerow([p1_name, score[0], p2_name, score[1], winner])
