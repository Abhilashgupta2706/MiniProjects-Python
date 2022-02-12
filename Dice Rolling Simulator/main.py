import random
import time

print('''Hi there, This is a Dice(s) rolling Simulator.
You can roll 1/2 dice(s)''')


# Choice of user to continue the game or not
def choice():
    user_choice = input("Do you want to roll dice again? (y/n) ").lower()
    if user_choice == 'y':
        rollTheDice()
    elif user_choice == "n":
        print('Hope you had fun playing this small game, See you again 👋🏻')
        return
    else:
        print('Wrong input try again!')
        choice()


# Logic
def rollTheDice():
    num_of_dices = input("\nHow many dies you want to roll? ")

    while True:
        if num_of_dices == '1':
            rollingPrint()
            dice = random.randint(1, 6)
            print(f'Rolled number is {dice}')
            choice()
            break

        elif num_of_dices == '2':
            rollingPrint()
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print(f'Rolled numbers are ({dice1},{dice2})')
            choice()
            break

        else:
            print("Invalid input! Choose between 1/2 dice(s) Only.")
            rollTheDice()


# Just a print Statement
def rollingPrint():
    print('Rolling....')
    time.sleep(1)


# Calling the Function
rollTheDice()
