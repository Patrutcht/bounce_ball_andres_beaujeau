from board import Board

WIDTH: int = 500
HEIGHT: int = 500


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
        self.target_score = target_score
        self.board = Board(width, height)
