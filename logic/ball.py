from pygame.math import Vector2
from pygame.color import Color
from numpy.matlib import sqrt


class Ball:
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

    def set_pos(self, x: float, y: float):
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

    def set_speed(self, x: float, y:float):
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

    def change_color(self, color:Color):
        """
        Change the color off the ball
        :param color: Color
        """

        ball_color = self.get_color()
        if ball_color != Color(255, 255, 255):
            self.set_color(color)
        else:
            self.set_color(Color(255, 255, 255))
