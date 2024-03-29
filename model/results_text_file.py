class ResultsTextFile:
    """ saves results of each game in a text file with the date and time, winner, and score of each player. """
    def __init__(self, file_path='results_of_othello.txt') -> None:
        self.file_path = file_path

    def save_results(self, results):
        with open(self.file_path, 'a') as f:
            f.write(results)