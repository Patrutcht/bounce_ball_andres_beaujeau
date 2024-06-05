import pygame
from pygame.math import Vector2
from pygame.color import Color
from numpy.matlib import sqrt
from player import Player
from abc import ABC


class Ball(ABC):
    """
    Handle all the ball logical
    """

    pos: Vector2
    speed: Vector2
    color: Color
    radius: int

    def __init__(self, x: int, y: int, color: Color, radius: int = 10):
        """
        Constructor of Ball
        :param x: x coordinate
        :param y: y coordinate
        :param color: color
        """

        self.pos = Vector2(x, y)
        self.speed = Vector2()
        self.color = color
        self.radius = radius

    def get_pos(self):
        """
        Get position of the ball
        :return: Vector2
        """

        return self.pos

    def set_pos(self, x: int, y: int):
        """
        Set the position of the ball
        :param x: float
        :param y: float
        """

        self.pos = Vector2(x, y)

    def get_speed(self):
        """
        Get speed of the ball
        :return: Vector2
        """

        return self.speed

    def set_speed(self, x: float, y: float):
        """
        Set speed of the ball
        :param x: float
        :param y: float
        """

        self.speed = Vector2(x, y)

    def get_color(self):
        """
        Get the color of the ball
        :return: Color
        """

        return self.color

    def set_color(self, color: Color):
        """
        Set the color of the ball
        :param color: Color
        """

        self.color = color

    def get_radius(self):
        """
        Get the radius of the ball
        :return: int
        """

        return self.radius

    def set_radius(self, radius: int):
        """
        Set the radius of the ball
        :param radius: int
        """

        self.radius = radius

    def dist(self, other):
        """
        Calculate the distance between a ball and another ball
        :param other: other ball
        :return: float
        """

        if other is None:
            return 0
        return self.pos.distance_to(other.pos)



    def draw(self, screen: pygame.Surface):
        """
        Draw the ball on the screen
        :param screen: pygame.Surface window to draw in
        """

        center = self.get_pos()
        radius = self.get_radius()
        color = self.get_color()
        pygame.draw.circle(screen, color, center, radius)


class white_Ball(Ball):

    """
    Handle white ball logical
    """
    player: Player
    def __init__(self, x, y, player: Player, color=Color(255, 255, 255)):
        super().__init__(x, y, color)
        self.player=player

    def get_player(self):
        """
        Get the number of the current player
        :return: Player
        """

        return self.player

    def set_player(self, player: Player):
        """
        Set the player using the white ball
        :param player: Player
        """

        self.player = player

class colored_Ball(Ball):
    """
        Handle colored ball logical
        """
    def __init__(self, x, y, color=Color(180, 180, 180)):
        super().__init__(x, y, color)


    def change_color(self, whiteball : white_Ball):
        """
        Change the color of the ball according to current player
        :param whiteball: white_Ball
        """

        ball_color = self.get_color()
        player_color=whiteball.get_player().getcolor()
        if ball_color != player_color :
            if ball_color == Color(180,180,180):
                ball_color = player_color
            else :
                ball_color = Color(180, 180, 180)
            self.set_color(player_color)



