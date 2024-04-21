import random


def game_round():
    n = str(input("Choose rock, paper or scissors: "))
    possible_actions = ["rock", "paper", "scissors"]
    a = random.choice(possible_actions)

    if n == a:
        print("Draw")
        return "d"
    elif n == "rock":
        if a == "scissors":
            print("Rock smashes Scissors. You Win!")
            return "p"
        else:
            print("Paper covers Rock. You Lose!")
            return "c"
    elif n == "paper":
        if a == "rock":
            print("Paper covers Rock. You Win!")
            return "p"
        else:
            print("Scissors cuts Paper. You Lose!")
            return "c"
    elif n == "scissors":
        if a == "rock":
            print("Rock smashes Scissors. You Lose")
            return "c"
        else:
            print("Scissors cuts Paper. You Win!")
            return "p"


result = game_round()
computer_score = 0
player_score = 0
if result == "c":
    computer_score = computer_score + 1
if result == "p":
    player_score = player_score + 1


play_again = str(input("Do you want to play again, y/n?"))
while play_again == "y":
    result = game_round()
    if result == "c":
        computer_score = computer_score + 1
    if result == "p":
        player_score = player_score + 1

    play_again = str(input("Do you want to play again, y/n?"))
print("player score = " + str(player_score) + " computer score = " + str(computer_score))

if computer_score > player_score:
    print("Computer Wins!")
elif player_score > computer_score:
    print("You Win!")
else:
    print("It's a draw!")