from __future__ import annotations
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


    def dist(self, other: Ball):
        """
        Calculate the distance between a ball and another ball
        :param other: other ball
        :return: float
        """

        if other is None:
            return 0
        return self.pos.distance_to(other.pos)
    