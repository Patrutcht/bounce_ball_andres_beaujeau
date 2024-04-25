from pygame import Color


class Player:
    """
    Handle logic of player
    """

    color: Color
    name: str
    score: int

    def __init__(self, name: str, color: Color):
        """
        Constructor of Player
        :param name: name of the player
        :param color: color of the player
        """

        self.name = name
        self.color = color
        self.score = 0

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
