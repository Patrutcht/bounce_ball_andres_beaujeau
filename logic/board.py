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
        :param ball: ball to check collision
        :return: Bool
        """

        balls = self.balls
        self.size.x=width
        self.size.y=height
        Ball.radius=radius

        if radius >= ball.pos.x or ball.pos.x >= width + radius:
            return self
        if radius >= ball.pos.y or ball.pos.y >= height + radius:
            return self
        for ball2 in balls:
            if ball2 == ball:
                continue
            if ball.dist(ball2) <= 2 * radius:
                return ball2
        return False

    def collision(self, ball: Ball):
        """
        Updates balls speed vector after collision between two balls
        :param ball:
        :return: None
        """

    if self.is_collide(ball):
        r = ball.radius
        x1 = ball.pos.x
        y1 = ball.pos.y
        vx1 = ball.speed.x
        vy1 = ball.speed.y
        if ball.radius >= ball.pos.x or ball.pos.x >= self.size.x + ball.radius:
            ball.speed.x = -vx1
        elif ball.radius >= ball.pos.y or ball.pos.y >= self.size.y + ball.radius:
            ball.speed.y = -vy1
        else:
            ball2 = self.is_collide(ball)
            x2 = ball2.pos.x
            y2 = ball2.pos.y
            vx2 = ball2.speed.x
            vy2 = ball2.speed.y

            # Calcul de la base orthonormée (n, g)
            # n est perpendiculaire au plan de collision, g est tangent
            nx = (x2 - x1) / (2 * r)
            ny = (y2 - y1) / (2 * r)
            gx = -ny
            gy = nx

            # Calcul des vitesses dans cette base
            v1n = nx * vx1 + ny * vy1
            v1g = gx * vx1 + gy * vy1
            v2n = nx * vx2 + ny * vy2
            v2g = gx * vx2 + gy * vy2

            # Permute les coordonnées n et conserve la vitesse tangentielle
            # Exécute la transformation inverse (base orthonormée => matrice transposée)
            ball.speed.x = nx * v2n + gx * v1g
            ball.speed.y = ny * v2n + gy * v1g
            ball2.speed.x = nx * v1n + gx * v2g
            ball2.speed.y = ny * v1n + gy * v2g

    def __create_ball(self, color: Color, radius: int = 10):
        """
        Create a ball that verify the  condition of no collision with other element
        :param color:
        :param radius:
        :return: Ball
        """

        ball = Ball(randrange(radius, self.size.x - radius), randrange(radius, self.size.y - radius), color, radius)
        collision = self.is_collide(ball)
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
        for n in range(nb_balls - 2):  # Generation of n-2 grey balls
            grey_ball = self.__create_ball(Color(190, 190, 190))
            self.balls.append(grey_ball)
        for n in range(2):  # Generation of 2 blue balls if we consider that Player2 is represented by the color blue
            # The second player start with two balls of his color
            blue_ball = self.__create_ball(Color(0, 0, 255))
            self.balls.append(blue_ball)
