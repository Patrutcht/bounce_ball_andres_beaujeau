import pygame
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

    def __init__(self, players, target_score: int, width: int = WIDTH, height: int = HEIGHT):
        """
        Constructor of Game
        :param nb_player: number of player
        :param target_score: score to reach
        """

        self.players = players
        self.target_score = target_score
        self.board = Board(width, height)

    def get_players(self):
        """
        Get the list of players
        :return: list[Player]
        """

        return self.players

    def set_players(self, players: list[Player]):
        """
        Set tje list of player
        :param players: list[Player] list of player
        """
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

    def get_board(self):
        """
        Get the board
        :return : Board.board
        """

        return self.board

    def draw(self, screen: pygame.Surface):
        """
        Draw the game on the pygame window
        :param screen: pygame.Surface
        """

        players = self.get_players()
        board = self.get_board()
        for player in players:
            player.draw()
        board.draw()
