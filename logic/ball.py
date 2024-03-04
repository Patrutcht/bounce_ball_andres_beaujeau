from pygame.math import Vector2
from pygame.color import Color


class Ball:
    """
    Handle all the ball logical
    """

    pos: Vector2
    speed: Vector2
    color: Color

    def __init__(self, x: int, y: int, color: Color):
        """
        Constructor of Ball
        :param x: x coordinate
        :param y: y coordinate
        :param color: color
        """

        self.pos = Vector2(x, y)
        self.speed = Vector2()
        self.color = color
    