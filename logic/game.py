from pygame import Color
from board import Board
from logic.player import Player

WIDTH: int = 500
HEIGHT: int = 500
BLUE = Color(0, 255, 0)
RED = Color(255, 0, 0)
GREEN = Color(0, 0, 255)
COLORS = [BLUE, RED, GREEN]

class Game:
    """
    Handle bounce ball game
    """
    players: list  # need Player object
    board: Board
    target_score: int

    def __init__(self, nb_player: int, target_score: int, width: int = WIDTH, height: int = HEIGHT):
        """
        Constructor of Game
        :param nb_player: number of player
        :param target_score: score to reach
        """

        self.players = []
        for n in range(nb_player):
            player_name = input(f'Player {n + 1} name: ')  # Ask each player their pseudo
            self.players.append(Player(player_name, COLORS[n]))
        self.target_score = target_score
        self.board = Board(width, height)

    def get_players(self):
        """
        Get the list of players
        :return: list[Player]
        """

        return self.players

    def get_target_score(self):
        """
        Get target score
        :return: int
        """

        return self.target_score

    def set_target_score(self, target_score: int):
        """
        Set target score
        """

        self.target_score = target_score