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
