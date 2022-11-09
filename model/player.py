from model.symbols import Symbols

class Player:
    """ represents a player of the game """
    def __init__(self, symbol: Symbols, board) -> None:
        self.symbol = symbol
        self.board = board