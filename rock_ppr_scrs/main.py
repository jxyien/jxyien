import random
import time

options = ("rock", "paper", "scissors")




choice_play = input('Do you want to play a game of rock, paper, scissors?: ')
running = None

if choice_play == "yes":
    running = True

elif choice_play == "no" or "nop":
    running = False


while running == True:

    player = None
    computer_inp = random.choice(options)

    while player not in options:
        player = input("Enter a choice: rock, paper or scissors?: ")
        time.sleep(2)
        print(f"Player: {player}")
        print(f"Computer: {computer_inp}")
    
    if player == computer_inp:
        time.sleep(2)
        print("It is a tie, amazing how you have stood against a computer!")

    elif player == "rock" and computer_inp == "scissors":
        time.sleep(2)
        print("You have beaten the computer! Congrats!")

    elif player == "scissors" and computer_inp == "rock":
        time.sleep(2)
        print("The computer has beaten you! =C")

    elif player == "paper" and computer_inp == "rock":
        time.sleep(2)
        print("You have beaten the computer! Congrats!")

    elif player == "rock" and computer_inp == "paper":
        time.sleep(2)
        print("The computer has beaten you! =C")

    elif player == "scissors" and computer_inp == "paper":
        time.sleep(2)
        print("You have beaten the computer! Congrats!")

    elif player == "paper" and computer_inp == "scissors":
        time.sleep(2)
        print("You have beaten the computer! Congrats!")

    break

# end
    
