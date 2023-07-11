from score import add_score
def welcome():
    name = input('Hello, what is your name?: ')
    print(f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.')

def load_game():
    print('1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n'
    "2. Guess Game - guess a number and see if you chose like the computer \n"
    '3. Currency Roulette - try and guess the value of a random amount of USD in ILS')
    while True:
        choose_game = input('Please choose a game to play: ')
        if choose_game.isdigit():
            choose_game = int(choose_game)
            if choose_game >= 1 and choose_game <= 3:
                print(f'your choose is: {choose_game}')
                break
            else:
                print('the game is not found')
        else:
            print("can't use a string")
    while True:
        choose_dif = input('Please choose game difficulty from 1 (easiest) to 5 (very hard):')
        if choose_dif.isdigit():
            choose_dif = int(choose_dif)
            if choose_dif >= 1 and choose_dif <= 5:
                print(f'your choose is: {choose_dif}')
                break
            else:
                print('incorrect difficult')
        else:
            print("can't use string")

    if choose_game == 1:
        from memorygame import play
        play(choose_dif)
    elif choose_game == 2:
        from guessgame import play
        play(choose_dif)
    elif choose_game == 3:
        from currencyroulettegame import play
        play(choose_dif)
    add_score(choose_dif)
