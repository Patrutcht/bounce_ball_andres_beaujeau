import pygame
from pygame import Color

COORDS = [(900, 150), (900, 400)]


class Player:
    """
    Handle logic of player
    """

    color: Color
    name: str
    score: int
    bot:bool

    def __init__(self, name: str, color: Color,bot):
        """
        Constructor of Player
        :param name: name of the player
        :param color: color of the player
        """

        self.name = name
        self.color = color
        self.score = 0
        self.bot = bot

    def get_name(self):
        """
        Get the name of the player
        :return: str
        """

        return self.name

    def set_name(self, name):
        """
        Set the name of the player
        :param name: str
        """

        self.name = name

    def get_score(self):
        """
        Get the score of the player
        :return: int
        """

        return self.score

    def set_score(self, score: int):
        """
        Set the score of the player
        :param score: int
        """

        self.score = score

    def get_color(self):
        """
        Get color of the player
        :return: Color
        """

        return self.color

    def set_color(self, color: Color):
        """
        Set the color of the ball
        :param color: Color
        """

        self.color = color
    def draw(self, screen: pygame.Surface, font: pygame.font):
        """
        Draw the player avatar and all his information on the display
        :param screen: pygama.Surface window to draw in
        :param font: pygame.font zone where the name of the player while be written
        """

        name = self.get_name()
        color = self.get_color()
        score = self.get_score()
        radius = 7
        if color.r == 255:
            p = 0
        else:
            p = 1
        if score > 0:
            for i in range(int((score + 1) / 2)):
                if score % 2 == 1:
                    pygame.draw.circle(screen, self.get_color(),
                                       (COORDS[p][0] + i * (5 + 2 * radius), COORDS[p][1] + 10),
                                       radius)
                    pygame.draw.circle(screen, self.get_color(),
                                       (COORDS[p][0] - i * (5 + 2 * radius), COORDS[p][1] + 10),
                                       radius)
                else:
                    pygame.draw.circle(screen, self.get_color(),
                                       (COORDS[p][0] + (2 * i + 1) * (5 / 2 + radius), COORDS[p][1] + 10),
                                       radius)
                    pygame.draw.circle(screen, self.get_color(),
                                       (COORDS[p][0] - (2 * i + 1) * (5 / 2 + radius), COORDS[p][1] + 10),
                                       radius)
        txt = font.render(name, True, pygame.Color(0, 0, 0))
        screen.blit(txt, (COORDS[p][0] - 40, COORDS[p][1] - 30))
