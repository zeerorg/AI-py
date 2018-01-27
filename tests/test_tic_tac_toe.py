"""
Testing Tic Tac Toe game
"""
from problems.tic_tac_toe import _Board, BoardQ2, BoardQ1

def run_game(go_first: bool, board_class: _Board):
    """
    Runs a game
    """
    board = board_class()
    player_moves = []
    while \
        not board.check_win(board.player) and \
        not board.check_win(board.computer) and \
        board.turn < 9:
        if board.turn % 2 == go_first:
            player_moves.append(board.get_random_blank())
            board.move_player(player_moves[-1])
        else:
            board.move_comp()
        board.turn += 1

    if board.check_win(board.player):
        print(board)
        print(player_moves)
        return False
    return True

NUM_TIME = 1000
def test_q1_0():
    """
    Test Q1 implementation
    """
    for _ in range(NUM_TIME):
        assert run_game(0, BoardQ1)

def test_q1_1():
    for _ in range(NUM_TIME):
        assert run_game(1, BoardQ1)

def test_q2_0():
    """
    Test Q1 implementation
    """
    for _ in range(NUM_TIME):
        assert run_game(0, BoardQ2)

def test_q2_1():
    for _ in range(NUM_TIME):
        assert run_game(1, BoardQ2)
