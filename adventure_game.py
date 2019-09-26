import time
import random
weapon_type = ["knife", "Swords", "Bow & Arrows"]
enemies = ["Darknut", "Garo Robe", "Sky Tail"]


def Print_Sleep(Print, Sleep):
    print(Print)
    time.sleep(Sleep)


def into():
    Print_Sleep("\n\n***----Wel Come to the Latest Adventure Game----***\n", 2)
    Print_Sleep("You find yourself in a deep well.", 2)
    Print_Sleep("After trying the whole day,you came out of the deep well.", 2)
    Print_Sleep("When you came out of the well, you found yourself in a dark "
                "forest.", 2)
    Print_Sleep("You feel scared in the dark forest,after walking a few steps "
                "you found a tiny knife on the grass", 2)
    Print_Sleep("There is a house in front of you, and a depot on your"
                " right side.", 2)
    Print_Sleep("You have both options to knock on the door of the house"
                " and to enter in the depot.", 2)


def forest():
    global choice
    choice = ""
    while choice != "1" and choice != "2":
        choice = input("Would you like to:\nKnock the Door Press (1)\n"
                       "Enter the Depot Press (2)\n")
        if choice == "1":
            house()
            choice = "2"
        elif choice == "2":
            Combat_Weapon()
        else:
            Print_Sleep("Invalid input.\n", 0)


def house():
    Print_Sleep("You approach the door of the house.", 2)
    Print_Sleep(f"You are about to knock when the door opens "
                "and out steps a "+enemie+" .", 2)
    Print_Sleep(f"Eep! This is the "+enemie+"'s house!", 2)
    final_stage()


def Combat_Weapon():
    global choice
    global weapon
    Print_Sleep("ew this is combat weapons depot,"
                " you see there is.", 1)
    Print_Sleep("1. Swords.\n"
                "2. Bow & Arrows\n", 0)
    choice = ""
    while choice != "1" and choice != "2":
        choice = input("You feel free to pick up any combat "
                       "weapon,Enter 1 ~ 2 \n")
        if choice == "1":
            weapon = "Swords"
            print("your weapon is "+weapon+".")
        elif choice == "2":
            weapon = "Bow & Arrows"
            print("your weapon is "+weapon+".")
    Print_Sleep("You walk back out to the forest.", 1)
    forest()


def final_stage():
    global choice
    global weapon
    Print_Sleep(f"The "+enemie+" attacks you!", 2)
    choice = ""
    if weapon == "knife":
        Print_Sleep(f"You feel a bit under-prepared for this,"
                    " what with only having a tiny "+weapon+".", 2)
        while choice != "1" and choice != "2":
            choice = input("Would you like to (1) fight or (2) run away?\n")
            if choice == "2":
                Print_Sleep("You run back into the forest."
                            " Luckily, you don't seem to "
                            "have been followed.", 2)
                forest()
        if choice == "1":
            if weapon == "knife":
                Print_Sleep(f"You do your best...", 1)
                Print_Sleep(f"but your" ' ' + weapon + " " "is no" ' '
                            "match for the" ' ' + enemie + ".", 2)
                Print_Sleep(f"You have been defeated!", 2)

    elif weapon == "Swords":
        Print_Sleep(f"As the "+enemie+" moves to attack,"
                    "you unsheath your new sword.", 2)
        Print_Sleep(f"The Sword shines brightly"
                    "in your hand as you brace yourself for the attack.", 3)
        Print_Sleep(f"But the "+enemie+" takes one look at"
                    " your shiny sword and runs away!", 3)
        Print_Sleep(f"You have rid the house of the"
                    " enemy. You are victorious!", 3)
    elif weapon == "Bow & Arrows":
        Print_Sleep(f"You are defeated! Bow and Arrows "
                    "are not effective for enemy", 1)
        Print_Sleep(f"But the sword has a magical power, so if you"
                    " used a sword, you could defeat the enemy!", 1)


def try_again():
    global choice
    while choice != "y" and choice != "n":
        choice = input("\nWould you like to play again? (y/n)\n")
        if choice == "n":
            Print_Sleep("Thanks for playing! See you next time.", 2)
            return "game_over"
        elif choice == "y":
            Print_Sleep("Excellent! Restarting the game ...", 2)
            return "run"


game_status = "run"

while game_status == "run":
    choice = ""
    game_status = "run"
    weapon = weapon_type[0]
    enemie = random.choice(enemies)
    into()
    forest()
    game_status = try_again()
