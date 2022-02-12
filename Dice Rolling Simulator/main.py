import random
import time

print('''Hi there, This is a Dice(s) rolling Simulator.
You can roll 1/2 dice(s)''')


def choice():
    user_choice = input("Do you want to roll dice again? (y/n) ").lower()
    if user_choice == 'y':
        rollTheDice()
    elif user_choice == "n":
        print('Hope you had fun playing this small game, See you again 👋🏻')

    else:
        print('Wrong input try again!')
        rollTheDice()


def rollTheDice():
    num_of_dices = int(input("\nHow many dies you want to roll? "))

    while True:
        if num_of_dices == 1:
            rollingPrint()
            dice = random.randint(1, 6)
            print(f'Rolled number is {dice}')
            choice()
            break

        elif num_of_dices == 2:
            rollingPrint()
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print(f'Rolled numbers are ({dice1},{dice2})')
            choice()
            break

        else:
            print("Choose between 1 and 2 dice(s) Only!")
            rollTheDice()


def rollingPrint():
    print('Rolling....')
    time.sleep(1)


rollTheDice()

# Python Projects

Collection of my Small Projects that I made with Python

I will update this repository as I will make new projects that will help me improve my coding skills as well as improve my problem solving.
If you have any suggestions on how to improve my code or a new project that I can build or anything else, please fell free to contact me.😊

# About Me

Here is my [Portfolio Website](https://www.abhilashgupta.ml/) where you will know everthing about me with my Resume ❤️