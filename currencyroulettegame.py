import random
import requests
from score import add_score

def get_money_interval(dif):
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        money_rate = data['rates']['ILS']
    print(f'USD rate: {money_rate}')
    sum_dol = random.randint(1, 100)
    print(f'amount of USD: {sum_dol}')
    usd_to_ils = sum_dol*money_rate
    money_interval = (usd_to_ils-(5-dif), usd_to_ils+(5-dif))
    return money_interval

def get_guess_from_user():
    while True:
        guess_from_user = input('How much ILS is it: ')
        if guess_from_user.isdigit():
            return int(guess_from_user)
        else:
            print('Invalid input.Only numbers')
#
def play(dif):
    while True:
        money_interval = get_money_interval(dif)
        guess_from_user = get_guess_from_user()
        if money_interval[0] <= guess_from_user <= money_interval[1]:
            print("Good job! Your answer is correct")
            add_score(dif)
        else:
            print("Sorry, it's incorrect answer")
        play_again = input('Want to play again? yes or no: ')
        if play_again == "no":
            next_game = input('Want to choose another game? yes or no: ')
            if next_game == "yes":
                from Live import load_game
                load_game()
            print("See you")
            break
        print("Let's go")