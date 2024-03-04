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

    def is_collide(self, ball: Ball):
        """
        Check if a ball collide with another ball or with the board
        :param ball: ball to check collision
        :return: Bool
        """

        if ball.radius >= ball.pos.x or ball.pos.x >= self.size.x + ball.radius:
            return True
        if ball.radius >= ball.pos.y or ball.pos.y >= self.size.y + ball.radius:
            return True
        for ball2 in self.balls:
            if ball2 == ball:
                continue
            if ball.dist(ball2) <= 2 * ball.radius:
                return True
        return False
