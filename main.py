from view.game_console_view import GameConsoleView
from controller.game_controller import GameController
from model.reversi_game import ReversiGame

board = GameConsoleView.welcome_message()
model = ReversiGame(board)
view = GameConsoleView(model)

controller = GameController(view, model)

controller.run_game() 
