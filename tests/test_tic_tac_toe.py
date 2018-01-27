"""
Testing Tic Tac Toe game
"""
from problems.tic_tac_toe import _Board, BoardQ2, BoardQ1

def run_game(go_first: bool, board_class: _Board) -> _Board:
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

    print(board)
    print(board.player)
    print(board.computer)
    print("\n")
    return board

def check_board(board: _Board):
    for move in board.player:
        assert move not in board.computer
    assert len(board.player) + len(board.computer) == 9 or board.check_win(board.player) or board.check_win(board.computer)

NUM_TIME = 100
def test_q1_0():
    """
    Test Q1 implementation
    """
    for _ in range(NUM_TIME):
        board = run_game(0, BoardQ1)
        check_board(board)

def test_q1_1():
    for _ in range(NUM_TIME):
        board = run_game(1, BoardQ1)
        check_board(board)

def test_q2_0():
    """
    Test Q1 implementation
    """
    for _ in range(NUM_TIME):
        board = run_game(0, BoardQ2)
        check_board(board)

def test_q2_1():
    for _ in range(NUM_TIME):
        board = run_game(1, BoardQ2)
        check_board(board)
