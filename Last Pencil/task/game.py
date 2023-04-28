import itertools
import random


def bot_play(p):
    if p == 1:
        # losing position
        rem_p = 1
    elif p % 4 == 0:
        # winning position
        rem_p = 3
    elif p % 4 == 1:
        # losing position
        rem_p = random.randint(1, 3)
    elif p % 4 == 2:
        # winning position
        rem_p = 1
    elif p % 4 == 3:
        # winning position
        rem_p = 2
    return rem_p


random.seed(123)
print("How many pencils would you like to use:")
finish = False
while not finish:
    try:
        pencils = int(input())
        if pencils == 0:
            print("The number of pencils should be positive")
        elif pencils < 0:
            print("The number of pencils should be numeric")
        else:
            finish = True
    except ValueError:
        print("The number of pencils should be numeric")

players = ["John", "Jack"]
iterlist = itertools.cycle(players)

print(f"Who will be the first ({players[0]}, {players[1]}):")
first_p = input()
while first_p not in players:
    print(f"Choose between {players[0]} and {players[1]}")
    first_p = input()

current_player = next(iterlist)
while current_player != first_p:
    current_player = next(iterlist)

while pencils > 0:
    print(pencils * "|")
    print(f"{current_player}'s turn")
    if current_player == players[0]:
        finish = False
        while not finish:
            try:
                rem_pencils = int(input())
                if rem_pencils not in [1, 2, 3]:
                    print("Possible values: '1', '2' or '3'")
                elif rem_pencils > pencils:
                    print("Too many pencils were taken")
                else:
                    finish = True
            except ValueError:
                print("Possible values: '1', '2' or '3'")
    else:
        rem_pencils = bot_play(pencils)
        print(rem_pencils)
    pencils -= rem_pencils
    current_player = next(iterlist)
    if pencils == 0:
        print(f"{current_player} won!")
