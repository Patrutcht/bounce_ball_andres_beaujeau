from random import randrange
from pygame import Color
from pygame.math import Vector2
from ball import Ball


class Board:
    """
    Handle logical of the board
    """
    size: Vector2  # x: width and y: height
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
        :param ball: Ball ball to check collision
        :return: Bool
        """

        balls = self.get_balls()
        width, height = self.get_size().x, self.get_size().y
        radius = ball.get_radius()
        ball_pos = ball.get_pos()
        if radius >= ball.pos.x or ball_pos.x >= width + ball.radius:
            return True
        if radius >= ball.pos.y or ball_pos.y >= height + ball.radius:
            return True
        for ball2 in balls:
            if ball2 == ball:
                continue
            if ball.dist(ball2) <= 2 * ball.radius:
                return True
        return False

    def __create_ball(self, color: Color, radius: int = 10):
        """
        Create a ball that verify the  condition of no collision with other element
        :param color: Color color of the ball to create
        :param radius: float radius of the ball to create
        :return: Ball
        """
        width, height = self.get_size().x, self.get_size().y
        ball = Ball(randrange(radius, width - radius), randrange(radius, height - radius), color, radius)
        collision = self.is_collide(ball)
        while collision:
            ball.set_pos(randrange(randrange(radius, width - radius), randrange(radius, height - radius)))
            collision = self.is_collide(ball)
        return ball

    def __init_balls(self, nb_balls: int):
        """
        Init a list of balls
        :param nb_balls: int number of balls to init
        """

        white_ball = self.__create_ball(Color(255, 255, 255), 8)
        self.balls.append(white_ball)
        for n in range(nb_balls - 2):  # Generation of n-2 grey balls
            grey_ball = self.__create_ball(Color(190, 190, 190))
            self.balls.append(grey_ball)
        for n in range(2):  # Generation of 2 blue balls if we consider that Player2 is represented by the color blue
            # The second player start with two balls of his color
            blue_ball = self.__create_ball(Color(0, 0, 255))
            self.balls.append(blue_ball)

    def get_size(self):
        """
        Get the size of the board
        :return: Vector2
        """

        return self.size

    def set_size(self, width: int, height:int):
        """
        Set the sire of the board
        :param width: int height of the board
        :param height: int width of the board
        """

        self.size = Vector2(width, height)

    def get_balls(self):
        """
        Get the list of all the balls on the board
        :return: list[Ball]
        """

        return self.balls

    def get_friction_coeff(self):
        """
        Get the friction coefficient of the balls on the board
        :return: float
        """

        return self.friction_coeff

    def set_friction_coeff(self, friction_coeff):
        """
        Set the friction coefficient of the balls on the board
        :param friction_coeff: float
        """

        self.friction_coeff = friction_coeff