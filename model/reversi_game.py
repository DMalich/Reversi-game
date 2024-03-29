from model.ai import AI
from model.board import Board
from model.symbols import Symbols

from datetime import datetime
from model.results_text_file import ResultsTextFile
from model.rules import Rules

from model.human import Human
from model.ai_minimax import AdvancedAI

class ReversiGame():
    """ this class represents the Reversi game, includes methods to run the game """
    
    #DIRECTIONS = [[0,1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    def __init__(self, board_size=8, file_path="results_of_game.txt") -> None:
        self.board_size = board_size
        self.board = Board(board_size)
        self.save_game = ResultsTextFile(file_path)
        self.rules = Rules(self.board, board_size)
        self.simple_ai = AI(Symbols.O, self.board, self.board_size)
        self.human = Human(Symbols, self.board, self.board_size)
        self.advanced_ai = AdvancedAI(Symbols.O, self.board, self.board_size)
        
    def new_board(self):
        """ displays a new board with four initial pieces """

        return self.board.new_board()

    def place_initial_pieces(self):
        """ places four starting pieces on the board """

        return self.board.initial_position()

    def write_results(self):
        """ saves results to a txt file """

        self.score = self.rules.calculate_score()
        today = datetime.now()
        time = today.strftime('%m/%d/%Y %H:%M:%S')
        self.results = f'Date and time of game: {time} | '
        self.results += f'Winner of game: {self.rules.winner} | '
        self.results += f'Player X: {self.score[0]}, Player O: {self.score[1]}\n'
        
        return self.save_game.save_results(self.results)