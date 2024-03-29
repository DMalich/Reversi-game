from copy import deepcopy
from model.rules import Rules
from model.symbols import Symbols

from model.player import Player


class Human(Player):
    """ defines a human player """
    
    def __init__(self, symbol: Symbols, board, board_size) -> None:
        super().__init__(symbol, board)
        self.rules = Rules(self.board, board_size)

    def give_hint(self, curr_player):
        lst_of_moves = self.rules.check_valid_moves(curr_player)

        if lst_of_moves == False:
            return 1

        board_copy = deepcopy(self.rules.board.mat)

        for row, col in lst_of_moves:
            board_copy[row-1][col-1] = 3

        return board_copy