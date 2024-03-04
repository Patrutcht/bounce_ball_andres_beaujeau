from pygame.math import Vector2
from ball import Ball


class Board:
    """
    Handle logical of the board
    """
    size: Vector2 # x: width and y: height
    balls: list[Ball]
    friction_coeff: float

    def __init__(self, width: int, height: int, friction: float = 0.2):
        """
        Constructor of Board
        :param width: width
        :param height: height
        :param friction: friction coefficient
        """

        self.size = Vector2(width, height)
        self.friction_coeff = friction
        self.balls = []
