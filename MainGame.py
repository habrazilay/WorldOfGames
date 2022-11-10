from Live import load_game, welcome
from CheckStatus import check_victory

player_name = "Daniel"  # input("Please enter you name: \n")
print(welcome(player_name))
check_victory(load_game())
