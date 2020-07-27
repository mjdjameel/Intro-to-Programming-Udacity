import time
import random


def print_sleep(mes, sec):
    print(mes)
    time.sleep(sec)


def main():
    Room_Colors = ["Red", "Blue", "Green", "Yellow", "Pink"]
    select = random.choice(Room_Colors)
    print_sleep("You find yourself locked in a " + select + " room.", 3.5)
    print_sleep("The room is empty and the door needs a combination "
                "code to be opened.", 3.5)
    print_sleep("So, your mission is to find the code to get "
                "out of the room.", 3.5)
    print_sleep("In front of you, there are a box and a locker.\n", 3.5)
    main_choice()


def box():
    print_sleep("You are reaching the box key.", 3.5)
    print_sleep("You are about to open the box.", 3.5)
    print_sleep("When you open the box, you find a piece of paper.\n", 3.5)
    box_choice()


def take_paper():
    print_sleep("\nThe combination code is ******", 3.5)
    print_sleep("Write the code at the door.", 3.5)
    print_sleep("Congratulations, you managed to get out of the room. ", 3.5)
    print_sleep("You are victorious", 3.5)
    play_again()


def leave_paper():
    print_sleep("You left the paper which contains the door "
                "combination code.", 3.5)
    print_sleep("You have been defeated", 3.5)
    play_again()


def locker():
    print_sleep("You are reaching the locker.", 3.5)
    print_sleep("You are about to open the locker.", 3.5)
    print_sleep("You find a key inside the locker.\n", 3.5)
    locker_choice()


def take_key():
    print_sleep("You took the key but the door doesn't need "
                "a key to open.", 3.5)
    print_sleep("You have been defeated", 3.5)
    play_again()


def leave_key():
    print_sleep("You choose to leave the key because the door "
                "doesn't need a key to open.\n", 3.5)
    main_choice()


def main_choice():
    print_sleep("Enter 1 to open the box.", 3.5)
    print_sleep("Enter 2 to open the locker.", 3.5)
    print_sleep("What would you like to do?", 3.5)
    user_input = input("(Please enter 1 or 2.)\n")
    while user_input != "1" or user_input != "2":
        if user_input == "1":
            box()
            break
        elif user_input == "2":
            locker()
            break
        else:
            user_input = input("(Please enter 1 or 2.)\n")


def box_choice():
    print_sleep("Enter 1 to take the paper.", 3.5)
    print_sleep("Enter 2 to leave the paper.", 3.5)
    user_input = input("(Please enter 1 or 2.)\n")
    while user_input != "1" or user_input != "2":
        if user_input == "1":
            take_paper()
            break
        elif user_input == "2":
            leave_paper()
            break
        else:
            user_input = input("(Please enter 1 or 2.)\n")


def locker_choice():
    print_sleep("Enter 1 to take the key.", 3.5)
    print_sleep("Enter 2 to leave the key.", 3.5)
    user_input = input("(Please enter 1 or 2.)\n")
    while user_input != "1" or user_input != "2":
        if user_input == "1":
            take_key()
            break
        elif user_input == "2":
            leave_key()
            break
        else:
            user_input = input("(Please enter 1 or 2.)\n")


def play_again():
    again = input("Would you like to play again? (y/n)\n")
    yes = {"y", "Y"}
    no = {"n", "N"}
    if again in yes:
        print_sleep("Excelent! Restarting the game...", 3.5)
        main()
    elif again in no:
        print_sleep("Thanks for playing! See you next time.", 3.5)
    else:
        play_again()


main()
