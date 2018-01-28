"""
Tic tac toe question 2 implementation
"""
import itertools

from problems.tic_tac_toe.base import _Board


class BoardQ2(_Board):
    """
    Question 2 board implementation
    """

    def move_comp(self):
        """
        Calculates and moves computer
        """
        if self.turn < 3:
            self.computer.append(self.get_random_blank())
            return

        for move_pair in itertools.chain(itertools.combinations(self.computer, 2), itertools.combinations(self.player, 2)):
            pair_sum_dif = 15 - sum(map(self.board.__getitem__, move_pair))
            if 0 < pair_sum_dif < 10:
                ind = self.board.index(pair_sum_dif)
                if ind not in self.computer and ind not in self.player:
                    self.computer.append(ind)
                    return
        self.computer.append(self.get_random_blank())
