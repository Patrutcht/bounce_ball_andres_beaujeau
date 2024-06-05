import csv
import numpy as np
import pygame
import button

# lien utile https://www.youtube.com/watch?v=2iyx8_elcYg
WIDTH = 1200
HEIGHT = 600
BOARD_WIDTH = 600
BOARD_HEIGHT = 600
COORDS = [(900, 150), (900, 400)]

pygame.init()
pygame.display.set_caption("Bounce Box")
icon = pygame.image.load('assets/image/icon.png')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.flip()
running = True
clock = pygame.time.Clock()


def dist(p1: pygame.Vector2, p2: pygame.Vector2):
    """
    Calculate the euclidian distance between two points
    :param p1: pygame.Vector2 first point
    :param p2: pygame.Vector2 second point
    :return: float
    """

    return np.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def angle(p1: pygame.Vector2, p2: pygame.Vector2):
    """
    Calculate the angle formed by a segment
    :param p1: pygame.Vector2
    :param p2: pygame.Vector2
    :return: float
    """

    return np.sign(np.arcsin((p1.y - p2.y) / dist(p1, p2))) * np.arccos((p1.x - p2.x) / dist(p1, p2))


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


menu = True
start = False
Player1 = False
Player2 = False
game = False
played_turn = False
p1_name = ""
p2_name = ""
player = None
c = 5
dt = 1/125
title = pygame.image.load('assets/image/title.png')
p1 = pygame.image.load('assets/image/player1.png')
p2 = pygame.image.load('assets/image/player2.png')
winner = False

play_img = pygame.image.load('assets/image.play.png').convert_alpha()
play_img = pygame.transform.scale(play_img, (300, 90))
start_img = pygame.image.load('assets/image/start.png').convert_alpha()
start_img = pygame.transform.scale(start_img, (300, 97))
next_img = pygame.image.load('assets/image/next.png').convert_alpha()
next_img = pygame.transform.scale(next_img, (300, 90))

# create button instances
play_button = button.Button(450, 250, play_img, 1)
start_button = button.Button(450, 350, start_img, 1)
next_button = button.Button(750, 350, next_img, 1)

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
        if i.type == pygame.KEYDOWN and not played_turn:
            if i.key == pygame.BUTTON_RIGHT:
                balls = game.board.get_balls()
                mouse_coord = pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                white_coord = game.board.get_balls[0].get_pos()
                dist = dist(mouse_coord, white_coord)
                white_ball = balls[0]
                white_ball.set_player(player)
                if dist < max_dist:
                    white_ball = balls.set_speed(c * mouse_coord)
                else:
                    white_ball = balls.set_speed(c * (max_dist * (
                            white_coord.x - mouse_coord.x) / dist - white_coord.x, max_dist * (
                                                                  white_coord.y - mouse_coord.y) / dist - white_coord.y))
                game.board.set_balls([white_ball] + balls[1:])

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
            Player1 = False
            start = True
    if start:
        screen.fill(pygame.Color(220, 220, 220))
        if not game:
            bounce_box = game([p1_name, p2_name], 5, BOARD_WIDTH, BOARD_HEIGHT)
            player = bounce_box.get_player()[0]
        elif not bounce_box.board.check_move() and not played_turn:
            game.draw()
            mouse_coord = pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            white_coord = game.board.get_balls[0].get_pos()
            phi = angle(mouse_coord, white_coord)
            dist = dist(mouse_coord, white_coord)
            if dist < max_dist:
                pygame.draw.polygon(screen, pygame.Color(185, 122, 87, 120), [mouse_coord, (
                    white_coord.x + radius * np.sin(phi), white_coord.y + radius * np.cos(phi)), (
                                                                                  white_coord.x - radius * np.sin(phi),
                                                                                  white_coord.y - radius * np.cos(
                                                                                      phi))])

            else:
                pygame.draw.polygon(screen, pygame.Color(185, 122, 87, 120), [(max_dist * (
                        white_coord.x - mouse_coord.x) / dist - white_coord.x, max_dist * (
                                                                                       white_coord.y - mouse_coord.y) / dist - white_coord.y),
                                                                              (white_coord.x + radius * np.sin(phi),
                                                                               white_coord.y + radius * np.cos(phi)), (
                                                                                  white_coord.x - radius * np.sin(phi),
                                                                                  white_coord.y - radius * np.cos(
                                                                                      phi))])
        elif not game.board.check_move() and played_turn:
            bounce_box.board.step(dt)
        elif game.board.check_move() and played_turn:
            player = bounce_box.get_players()[abs(1 - 1**bounce_box.get_players().index(player))]
    pygame.display.flip()

if winner:
    with open('assets/game_stats.csv', 'a', newline='') as f:
        stats = csv.writer(f, delimiter=';')
        stats.writerow([p1_name, p2_name, winner])
