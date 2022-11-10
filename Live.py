import GuessGame
import MemoryGame
import CurrencyRoulleteGame
from CheckInput import check_input


def welcome(name: str):
    print("Hello " + name + " and welcome to the World of Games (WoG)."'\n'"Here you can find many cool games to play.")


def load_game():
    print('Please choose a game to play: \n'
          '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it\n'
          '2. Guess Game - guess a number and see if you chose like the computer\n'
          '3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n')
    game_number = check_input(3)
    print("Please choose game difficulty from 1 to 5: "'\n')
    game_difficulty = check_input(5)
    status = False
    if game_number == 1:
        status = MemoryGame.play(game_difficulty)
    elif game_number == 2:
        status = GuessGame.play(game_difficulty)
    elif game_number == 3:
        status = CurrencyRoulleteGame.play(game_difficulty)

    return status


class GameClass:

    def __init__(self, game_number, description, difficulty, module):
        self.game_number = game_number
        self.description = description
        self.difficulty = difficulty
        self.module = module
        pass

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        pass


guess_game = GameClass
memory_game = GameClass
currency_roulette = GameClass

