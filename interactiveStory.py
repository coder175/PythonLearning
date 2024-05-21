import time
import fontstyle
import random

f = fontstyle
t = time
r = random


def loading():
    randomTicks = random.choice([1, 2, 3])
    for x in range(1, (3 + randomTicks) + 1):
        if x % 3 == 0:
            print(f.apply("■", "bold"), end=" ")
            t.sleep(0.5)
            print("\b \b \b" * 7, end=" ")
        elif x % 3 == 1:
            t.sleep(0.5)
            print(" ", end="")
            print(f.apply("■", "bold"), end=" ")
            t.sleep(0.25)
        else:
            print(f.apply("■", "bold"), end=" ")
            t.sleep(0.25)

    print(" ", end="\r")
    print("                              ", end="\r")


def splitpath(optionList, question):
    userAns = input(f.apply(question, "bold green green_bg") + " ")
    t.sleep(1)
    while userAns not in optionList:
        print(f.apply(f"You typed '{userAns}'", "bold yellow yellow_bg") + " ")
        t.sleep(1)
        print(f.apply(f"Please type either {', '.join(str(x) for x in optionList[:-1])}, or {optionList[-1]} ", "bold red red_bg"))
        t.sleep(1)
        userAns = input(f.apply(question, "bold green green_bg") + " ")
        t.sleep(1)


print(f.apply(" Welcome to the Story!", "bold green green_bg"))
print(" ")
t.sleep(1)
name = input("What is your name? ")
name = name.replace(" ", "")
print("")
t.sleep(2)
print(f.apply(f" Okay, {name}! Here is the story:", "bold green green_bg"))
print(" ")
t.sleep(1)
print("You wake up in a room.")
t.sleep(2)
print("You don't remember anything.")
t.sleep(2)
print("There is a single lightbulb flickering at the top of the room, about 2 feet above your head.")
t.sleep(2)
print(f"In your pocket, you see a piece of paper with a name on it: {f.apply(name, 'bold red')}.", end="  ")
t.sleep(2)
print("You assume that would be your name.")
t.sleep(2)
print("In front of you, there are 3 things: ")
t.sleep(2)
print("    A sword")
t.sleep(2)
print("    A cinderblock")
t.sleep(2)
print("    A flashlight")
t.sleep(2)
splitpath([1, 2, 3], "What should you pick up? Type '1' for a sword, '2' for a cinderblock, and '3' for a flashlight. ")
