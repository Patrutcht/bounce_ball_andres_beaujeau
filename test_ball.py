import unittest
import pygame
from pygame.color import Color
from pygame.math import Vector2
from ball import Ball, white_Ball, colored_Ball
from player import Player
class TestBall(unittest.TestCase):

    def setUp(self):
        self.ball = Ball(0, 0, Color(255, 0, 0), 14)

    def test_get_pos(self):
        self.assertEqual(self.ball.get_pos(), Vector2(0, 0))

    def test_set_pos(self):
        self.ball.set_pos(10, 20)
        self.assertEqual(self.ball.get_pos(), Vector2(10, 20))

    def test_get_speed(self):
        self.assertEqual(self.ball.get_speed(), Vector2(0, 0))

    def test_set_speed(self):
        self.ball.set_speed(5, 10)
        self.assertEqual(self.ball.get_speed(), Vector2(5, 10))

    def test_get_color(self):
        self.assertEqual(self.ball.get_color(), Color(255, 0, 0))

    def test_set_color(self):
        self.ball.set_color(Color(0, 255, 0))
        self.assertEqual(self.ball.get_color(), Color(0, 255, 0))

    def test_get_radius(self):
        self.assertEqual(self.ball.get_radius(), 14)

    def test_set_radius(self):
        self.ball.set_radius(20)
        self.assertEqual(self.ball.get_radius(), 20)

    def test_dist(self):
        other_ball = Ball(0, 0, Color(0, 0, 255), 14)
        self.assertEqual(self.ball.dist(other_ball), 0)
        other_ball.set_pos(3, 4)
        self.assertEqual(self.ball.dist(other_ball), 5)

class TestWhiteBall(unittest.TestCase):

    def setUp(self):
        self.white_ball = white_Ball(0, 0, 14, Color(255, 255, 255))
        self.player = Player('name',Color(255, 0, 0))

    def test_get_player(self):
        self.assertIsNone(self.white_ball.get_player())

    def test_set_player(self):
        self.white_ball.set_player(self.player)
        self.assertEqual(self.white_ball.get_player(), self.player)

class TestColoredBall(unittest.TestCase):

    def setUp(self):
        self.colored_ball = colored_Ball(0, 0, Color(120, 120, 120))
        self.white_ball = white_Ball(0, 0, 14, Color(255, 255, 255))
        self.player1 = Player('name',Color(0, 255, 0))
        self.player2 = Player('name', Color(255, 0, 0))

    def test_change_color(self):
        self.white_ball.set_player(self.player1)
        self.colored_ball.change_color(self.white_ball)
        self.assertEqual(self.colored_ball.get_color(), Color(0, 255, 0))
        self.white_ball.set_player(self.player2)
        self.colored_ball.change_color(self.white_ball)
        self.assertEqual(self.colored_ball.get_color(), Color(120, 120, 120))


if __name__ == '__main__':
    unittest.main()