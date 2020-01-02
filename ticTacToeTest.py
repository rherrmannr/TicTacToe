import unittest
from ticTacToe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe("X")

    def test_empty_game_field(self):
        for row in self.game.gf:
            for ele in row:
                self.assertEqual(ele, None)

    def test_set_player(self):
        self.game.set_obj(0, 0, "O")
        self.game.set_obj(1, 0, "O")
        self.game.set_obj(2, 0, "O")
        self.game.set_obj(0, 1, "X")
        self.game.set_obj(1, 1, "X")
        self.game.set_obj(2, 1, "X")
        self.game.set_obj(0, 2, "O")
        self.game.set_obj(1, 2, "O")
        self.game.set_obj(2, 2, "O")
        self.assertEqual(self.game.gf,
                         [["O", "X", "O"],
                          ["O", "X", "O"],
                          ["O", "X", "O"]])

    def test_set_only_once(self):
        self.assertTrue(self.game.set_obj(0, 0, "X"))
        self.assertFalse(self.game.set_obj(0, 0, "X"))
        self.assertFalse(self.game.set_obj(0, 0, "O"))

    def test_won_empty(self):
        # test empty game field
        self.assertEqual(self.game.check_player_has_won(), None)

    def test_won_row(self):
        # test row
        self.game.gf = [["X", "X", "X"],
                        ["O", "O", None],
                        [None, None, None]]
        self.assertEqual(self.game.check_player_has_won(), "X")

    def test_won_column(self):
        # test column
        self.game.gf = [["X", "X", "O"],
                        ["X", "O", None],
                        ["X", None, None]]
        self.assertEqual(self.game.check_player_has_won(), "X")

    def test_won_top_left_bottom_right(self):
        # test top left to bottom right
        self.game.gf = [["X", "X", "O"],
                        ["X", "O", None],
                        ["X", None, None]]
        self.assertEqual(self.game.check_player_has_won(), "X")

    def test_won_bottom_left_top_right(self):
        # test bottom left to top right
        self.game.gf = [["X", "X", "O"],
                        ["X", "O", None],
                        ["X", None, None]]
        self.assertEqual(self.game.check_player_has_won(), "X")

    def test_won_draw(self):
        # test draw
        self.game.gf = [["X", "X", "O"],
                        ["O", "O", "X"],
                        ["X", "O", "X"]]
        self.assertEqual(self.game.check_player_has_won(), None)

    def test_check_draw_false(self):
        self.game.gf = [["X", "X", None],
                        ["O", "O", "X"],
                        ["X", "O", "X"]]
        self.assertFalse(self.game.check_draw())

    def test_check_draw_true(self):
        self.game.gf = [["X", "X", "O"],
                        ["O", "O", "X"],
                        ["X", "O", "X"]]
        self.assertTrue(self.game.check_draw())


if __name__ == '__main__':
    unittest.main()
