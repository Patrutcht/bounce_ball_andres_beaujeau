from logic.ball import Ball
import unittest
from pygame.color import Color
from pygame.math import Vector2


class TestBall(unittest.TestCase):

    def test_init(self):
        b = Ball(2, 3, Color(255, 255, 255))
        self.assertEqual(b.pos, Vector2(2, 3))
        self.assertEqual(b.speed, Vector2(0, 0))
        self.assertEqual(b.color, Color(255, 255, 255))
        self.assertEqual(b.radius, 10)

    def test_get_color(self):
        b = Ball(2, 3, Color(255, 0, 255))
        b2 = Ball(5, 3, Color(0, 0, 255))
        self.assertEqual(b.get_color(), Color(255, 0, 255))
        self.assertEqual(b2.get_color(), Color(0, 0, 255))

    def test_set_color(self):
        b = Ball(2, 3, Color(255, 0, 255))
        self.assertEqual(b.color, Color(255, 0, 255))
        b.set_color(Color(0, 0, 255))
        self.assertEqual(b.color, Color(0, 0, 255))

    def test_dist(self):
        b = Ball(2, 3, Color(255, 0, 255))
        b2 = Ball(22, 3, Color(255, 0, 255))
        self.assertEqual(b.dist(b2), 20)
        self.assertEqual(b2.dist(None), 0)

    def test_change_color(self):
        b = Ball(2, 3, Color(255, 0, 255))
        b2 = Ball(10, 6, Color(255, 255, 255))
        b.change_color(Color(0, 0, 255))
        b2.change_color(Color(255, 0, 0))
        self.assertEqual(b.color, Color(0, 0, 255))
        self.assertEqual(b2.color, Color(255, 255, 255))


if __name__ == '__main__':
    unittest.main()
