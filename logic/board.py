from random import randrange
from pygame import Color
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
        self.__init_balls(11)

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

    def __create_ball(self, color: Color, radius: int = 10):
        """
        Create a ball that verify the  condition of no collision with other element
        :param color:
        :param radius:
        :return: Ball
        """

        ball = Ball(randrange(radius, self.size.x - radius), randrange(radius, self.size.y - radius), color, radius)
        collision = self.is_collide(ball)
        if collision:
            while collision:
                ball = Ball(randrange(radius, self.size.x - radius), randrange(radius, self.size.y - radius), color, radius)
                collision = self.is_collide(ball)
        return ball

    def __init_balls(self, nb_balls: int):
        """
        Init a list of balls
        :param nb_balls: number of balls to init
        """

        white_ball = self.__create_ball(Color(255, 255, 255), 8)
        self.balls.append(white_ball)
        for n in range(nb_balls - 2): # Generation of n-2 grey balls
            grey_ball = self.__create_ball(Color(190, 190, 190))
            self.balls.append(grey_ball)
        for n in range(2): # Generation of 2 blue balls if we consider that Player2 is represented by the color blue
            # The second player start with two balls of his color
            blue_ball = self.__create_ball(Color(0, 0, 255))
            self.balls.append(blue_ball)