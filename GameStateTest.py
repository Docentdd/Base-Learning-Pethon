import unittest

from scipy.special import expected

import SnakeGame


class MyTestCase(unittest.TestCase):
    def snake_should_move_right(self):
        state = SnakeGame.GameState(
            snake=[SnakeGame.Position(0, 0), SnakeGame.Position(0, 1), SnakeGame.Position(0, 2)],
            direction = SnakeGame.Direction.RIGHT,
            food = SnakeGame.Position(10,10),
            field_size=20
        )
        state.step()
        expected = [SnakeGame.Position(0,1), SnakeGame.Position(0,2), SnakeGame.Position(0,3)]
        self.assertEqual(expected, state.snake)
    def snake_should_move_left(self):
        state = SnakeGame.GameState(
            snake=[SnakeGame.Position(1, 2), SnakeGame.Position(1, 3), SnakeGame.Position(1, 4)],
            direction = SnakeGame.Direction.RIGHT,
            food = SnakeGame.Position(10,10),
            field_size=20
        )
        state.step()
        expected = [SnakeGame.Position(1,3), SnakeGame.Position(1,4), SnakeGame.Position(0,4)]
        self.assertEqual(expected, state.snake)
    def snake_should_move_up(self):
        state = SnakeGame.GameState(
            snake =[SnakeGame.Position(1,2), SnakeGame.Position(1,3), SnakeGame.Position(1,4)],
            direction = SnakeGame.Direction.UP,
            food = SnakeGame.Position(10,10),
            field_size=20
        )
        state.step()
        expected = [SnakeGame.Position(1,1), SnakeGame.Position(1,2), SnakeGame.Position(1,3)]
        self.assertEqual(expected, state.snake)

    def snake_should_move_down(self):
        state = SnakeGame.GameState(
            snake =[SnakeGame.Position(1,2), SnakeGame.Position(1,3), SnakeGame.Position(1,4)],
            direction = SnakeGame.Direction.DOWN,
            food = SnakeGame.Position(10,10),
            field_size=20
        )
        state.step()
        expected = [SnakeGame.Position(1,3), SnakeGame.Position(1,4), SnakeGame.Position(1,5)]
        self.assertEqual(expected, state.snake)

if __name__ == '__main__':
    unittest.main()
