from abc import ABC, abstractmethod
from model.reversi_game import ReversiGame

class GameView(ABC):
    def __init__(self, game) -> None:
        self.game = game

    @staticmethod
    def welcome_message():
        pass

    @abstractmethod
    def player_options(self):
        pass

    @abstractmethod
    def invalid_choice(self):
        pass
    
    @abstractmethod
    def get_move(self):
        pass

    @abstractmethod
    def draw_board(self):
        pass

    @abstractmethod
    def display_turn(self):
        pass

    @abstractmethod
    def display_winner(self, player):
        pass

    @abstractmethod
    def display_score(self, score):
        pass

    @abstractmethod
    def invalid_move(self):
        pass

    @abstractmethod
    def display_exit_message(self):
        pass

    @abstractmethod
    def display_computer_turn(self):
        pass
    
    @abstractmethod
    def display_play_again(self):
        pass 

    @abstractmethod
    def display_empty_line(self):
        pass

    @abstractmethod
    def no_moves(self):
        pass

    @abstractmethod
    def display_rules(self):
        pass

    @abstractmethod
    def get_depth(self):
        pass