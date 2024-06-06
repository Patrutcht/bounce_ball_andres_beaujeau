import unittest
from unittest.mock import Mock
from pygame import Color
from pygame.math import Vector2
from ball import Ball, white_Ball, colored_Ball
from board import Board
from player import Player


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board(800, 600, 100)

    def test_init_balls(self):
        self.assertEqual(len(self.board.get_balls()), 12)  # Check initial number of balls

    def test_is_collide_no_collision(self):
        ball = Ball(50, 50, Color(255, 0, 0), 14)
        self.board.set_balls([ball])
        self.assertFalse(self.board.is_collide(ball))

    def test_is_collide_with_wall(self):
        ball = Ball(10, 10, Color(255, 0, 0), 14)
        self.board.set_balls([ball])
        self.assertTrue(self.board.is_collide(ball))

    def test_is_collide_with_another_ball(self):
        ball1 = Ball(50, 50, Color(255, 0, 0), 14)
        ball2 = Ball(60, 50, Color(0, 255, 0), 14)
        self.board.set_balls([ball1, ball2])
        self.assertTrue(self.board.is_collide(ball1))

    def test_collision_wall(self):
        ball = Ball(10, 10, Color(255, 0, 0), 14)
        ball.set_speed(100, 0)
        self.board.set_balls([ball])
        self.board.collision(ball)
        self.assertEqual(ball.get_speed(), Vector2(-100, 0))

    def test_collision_ball(self):
        player = Player('name',Color(0, 255, 0))
        white_ball = white_Ball(50, 50, 14)
        white_ball.set_player(player)
        colored_ball = colored_Ball(64, 50, Color(120, 120, 120))

        self.board.set_balls([white_ball, colored_ball])
        self.board.collision(white_ball)
        self.assertEqual(colored_ball.get_color(), Color(0, 255, 0))

    def test_get_size(self):
        self.assertEqual(self.board.get_size(), Vector2(800, 600))

    def test_set_size(self):
        self.board.set_size(1024, 768)
        self.assertEqual(self.board.get_size(), Vector2(1024, 768))

    def test_get_balls(self):
        self.assertEqual(len(self.board.get_balls()), 12)

    def test_set_balls(self):
        ball = Ball(50, 50, Color(255, 0, 0), 14)
        self.board.set_balls([ball])
        self.assertEqual(self.board.get_balls(), [ball])

    def test_del_ball(self):
        ball1 = Ball(50, 50, Color(255, 0, 0), 14)
        ball2 = Ball(60, 50, Color(0, 255, 0), 14)
        self.board.set_balls([ball1, ball2])
        self.board.del_ball(ball1)
        self.assertEqual(self.board.get_balls(), [ball2])

    def test_get_friction_coeff(self):
        self.assertEqual(self.board.get_friction_coeff(), 100)

    def test_set_friction_coeff(self):
        self.board.set_friction_coeff(200)
        self.assertEqual(self.board.get_friction_coeff(), 200)

    def test_check_move(self):
        ball1 = Ball(50, 50, Color(255, 0, 0), 14)
        ball2 = Ball(60, 50, Color(0, 255, 0), 14)
        ball1.set_speed(10, 0)
        ball2.set_speed(0, 0)
        self.board.set_balls([ball1, ball2])
        self.assertTrue(self.board.check_move())

    def test_check_no_move(self):
        ball1 = Ball(50, 50, Color(255, 0, 0), 14)
        ball2 = Ball(60, 50, Color(0, 255, 0), 14)
        ball1.set_speed(0, 0)
        ball2.set_speed(0, 0)
        self.board.set_balls([ball1, ball2])
        self.assertFalse(self.board.check_move())

    def test_draw(self):
        # This test is difficult to implement without a visual confirmation
        # or a more complex setup that mocks pygame's draw functions.
        pass

    def test_step(self):
        ball = Ball(50, 50, Color(255, 0, 0), 14)
        ball.set_speed(1000, 0)
        self.board.set_balls([ball])
        self.board.step(0.1)
        self.assertEqual(ball.get_speed(), Vector2(990, 0))
        self.assertEqual(ball.get_pos(), Vector2(149, 50))
        ball.set_speed(10, 0)
        self.board.step(0.1)
        self.assertEqual(ball.get_speed(), Vector2(0, 0))



if __name__ == '__main__':
    unittest.main()