import unittest
from FocusGame import FocusGame


class FocusGameTests(unittest.TestCase):
    def test_the_initializer_of_FocusGame_creates_a_FocusGame_object_when_passed_valid_parameters(self):
        g = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        self.assertIsInstance(g, FocusGame)

    def test_the_initializer_of_FocusGame_does_not_create_a_FocusGame_object_when_passed_no_parameters(self):
        def f():
            g = FocusGame()

        self.assertRaises(TypeError, f)

    def test_that_an_empty_board_is_created_when_FocusGame_is_initialized(self):
        g = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        self.assertIsInstance(g._board, list)

    def test_that_move_piece_method_accepts_4_parameters(self):
        g = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        s = g.move_piece('PlayerA', (0, 0), (0, 1), 1)
        self.assertEqual(s, "successfully moved")

    def test_that_there_is_a_reserve_pile_which_is_emtpy_when_game_is_created(self):
        g = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))

    def test_that_when_a_stack_is_more_than_5_pieces_high_move_pieces_to_capture_and_reserve_piles(self):
        pass

    def show_reserve_returns_0_when_no_moves_have_been_made(self):
        pass

    def show_reserve_returns_the_correct_count_when_move_resulting_in_one_piece_put_in_reserve_pile(self):
        pass

    '''
    def test_that_multiple_move_can_be_performed_to_create_stack_of_4_pieces(self):
        g = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))

        #player1 moves - g.move_piece()
        ##g.move_piece()
        #player2 move
        #player1 move
        #player2 move
        #player1 move
    '''


if __name__ == '__main__':
    unittest.main()