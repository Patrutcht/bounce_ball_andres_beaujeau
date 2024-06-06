from random import randrange

import pygame
from pygame import Color
from pygame.math import Vector2
from ball import Ball, white_Ball, colored_Ball


class Board:
    """
    Handle logical of the board
    """
    size: Vector2  # x: width and y: height
    balls: list[Ball]
    friction_coeff: float

    def __init__(self, width: int, height: int, friction: float = 0.5):
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
        if radius >= ball.pos.x or ball_pos.x >= width - ball.radius:
            return True
        if radius >= ball.pos.y or ball_pos.y >= height - ball.radius:
            return True
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
            ball_pos=ball.get_pos()
            ball_speed=ball.get_speed()
            x1 = ball_pos.x
            y1 = ball_pos.y
            vx1 = ball_speed.x
            vy1 = ball_speed.y
            if r >= x1 or x1 >= self.size.x - r:
                ball.set_speed(-vx1,vy1)
            elif r >= y1 or y1 >= self.size.y - r:
                ball.set_speed(vx1,-vy1)
            else:
                ball2 = self.is_collide(ball)
                delete_ball1, delete_ball2 = False, False
                if type(ball) == white_Ball:
                    player_color = ball.get_player().get_color()
                    ball_color = ball2.get_color()
                    if player_color == ball_color:
                        delete_ball2 = True
                    else:
                        ball2.change_color(ball)

                if type(ball2) == white_Ball:
                    player_color = ball2.get_player().get_color()
                    ball_color = ball.get_color()
                    if player_color == ball_color:
                        delete_ball1 = True
                    else:
                        ball.change_color(ball2)

                ball2 = self.is_collide(ball)
                x2 = ball2.get_pos().x
                y2 = ball2.get_pos().y
                vx2 = ball2.get_speed().x
                vy2 = ball2.get_speed().y

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

                if delete_ball1:
                    self.del_ball(ball)
                    self.get_balls()[0].get_player().set_score(self.get_balls()[0].get_player().get_score() + 1)
                if delete_ball2:
                    self.del_ball(ball2)
                    self.get_balls()[0].get_player().set_score(self.get_balls()[0].get_player().get_score() + 1)

    def __create_ball(self, color: Color, radius: int = 10):
        """
        Create a ball that verify the  condition of no collision with other element
        :param color: Color color of the ball to create
        :param radius: float radius of the ball to create
        :return: Ball
        """
        width, height = self.get_size().x, self.get_size().y
        ball = colored_Ball(randrange(radius, width - radius), randrange(radius, height - radius), color)
        collision = self.is_collide(ball)
        while collision:
            ball.set_pos(randrange(randrange(radius, width - radius)), randrange(radius, height - radius))
            collision = self.is_collide(ball)
        return ball

    def __init_balls(self, nb_balls: int):
        """
        Init a list of balls
        :param nb_balls: int number of balls to init
        """
        radius = 14
        width, height = self.get_size().x, self.get_size().y
        whiteball = white_Ball(randrange(radius, width - radius), randrange(radius, height - radius), radius)
        self.balls.append(whiteball)
        for n in range(nb_balls - 2):  # Generation of n-2 grey balls
            grey_ball = self.__create_ball(pygame.Color(120, 120, 120))
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

    def set_size(self, width: int, height: int):
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

    def set_balls(self, balls):
        """
        Set the balls on the board
        :param balls: list[Ball] balls to add to the setter
        """

        self.balls = balls

    def del_ball(self, ball):
        """
        Delete the ball from the list of balls present on the board
        :param ball: Ball ball to delete
        """

        balls_on_board = self.get_balls()
        ind = balls_on_board.index(ball)
        balls_on_board.pop(ind)
        self.set_balls(balls_on_board)

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

    def check_move(self):
        """
        Check if the balls are still moving
        :return: Bool True if at least a ball is moving
        """

        balls = self.get_balls()
        for ball in balls:
            speed = ball.get_speed()
            if speed.length() != 0:
                return True
        return False

    def draw(self, screen: pygame.Surface):
        """
        Draw the board on the screen
        :param screen: pygame.Surface window to draw in
        """

        size = self.get_size()
        balls = self.get_balls()
        black_rect = pygame.Rect((0, 0), (size[0] + 30, size[1] + 30))
        yellow_rect = pygame.Rect((10, 10), (size[0] + 10, size[1] + 10))
        green_rect = pygame.Rect((15, 15), size)
        pygame.draw.rect(screen, Color(102, 63, 65), black_rect)
        pygame.draw.rect(screen, Color(184, 162, 0), yellow_rect)
        pygame.draw.rect(screen, Color(14, 109, 1), green_rect)
        for ball in balls:
            ball.draw(screen)

    def step(self, dt: float):

        balls = self.get_balls()
        friction_coeff = self.get_friction_coeff()
        for ball in balls:
            if self.is_collide(ball):
                self.collision(ball)
            ball_pos = ball.get_pos()
            ball_speed = ball.get_speed()
            if Vector2.length(ball_speed) != 0.0:
                ball_direction = Vector2.normalize(ball_speed)
                friction_force = -friction_coeff * ball_direction
                new_speed = ball_speed + dt * friction_force
                if Vector2.length(ball_speed) <= 0.2:
                    ball.set_speed(0, 0)
                else:
                    ball.set_speed(new_speed.x, new_speed.y)
                ball_speed = ball.get_speed()
                new_pos = ball_pos + dt * ball_speed
                ball.set_pos(new_pos.x, new_pos.y)
            else :
                ball.set_speed(0, 0)
