# import random
from rich import *
from rich.console import Console
from time import sleep
import sys

console = Console()

def loading(time):
    for x in range(1, 3 + time):
        if x % 3 == 0:
            print("■", end=" ")
            sleep(0.5)
            sys.stdout.write('\r' + ' ' * 20 + '\r')
            sys.stdout.flush()

        elif x % 3 == 1:
            sleep(0.5)
            print(" ", end="")
            print("■", end=" ")
            sleep(0.25)
        else:
            print("■", end=" ")
            sleep(0.25)

    sys.stdout.write('\r' + ' ' * 20 + '\r')
    sys.stdout.flush()

def choice(question, choices):
    print("\t" + question)
    sleep(1.5)
    for index, value in enumerate(choices):
        print("\t" + choices[index] + f"[bold red] Press [{index + 1}]")
        sleep(1.5)

    choice_answer = console.input("[bold red]What do you choose? ")
    choice_answer.replace(" ", "")

    while not choice_answer.isdigit() or int(choice_answer) not in range(1, len(choices) + 1):
        print(f"[bold yellow reverse]You typed: '{choice_answer}'. Your options are: {', '.join(choices)}")
        choice_answer = console.input("[bold red]What do you choose? ")
        choice_answer = choice_answer.replace(" ", "")

    return int(choice_answer)


print("[bold red reverse]You wake up in a prison.")
sleep(2.5)
print('[bold]There is only one thought in your mind: [red]"Escape"')
sleep(2)
print('[bold]You are sentenced to [red]death[/red] tomorrow morning, so you need to get out.')
sleep(2)
print('[bold]The guards just passed your room.')
sleep(2.5)

choiceReturn = choice("Do You:", ["Escape now", "Wait Until Nightfall"])
sleep(1)
loading(2)
if choiceReturn == 1: # Escape Now
    print("First, you need a way to get out.")
    sleep(2)
    print("Fortunately, you've been planning a way out for a long time.")
    sleep(2)
    print("You have 3 ways out.")
    sleep(1)
    choiceReturn = choice("You Can:", ["Try To Pick the Lock", "Climb out the Window", "Dig out of the prison"])
    sleep(1)
    loading(2)
    if choiceReturn == 1: # Pick the Lock
        print("")
    elif choiceReturn == 2: #Climb out the Window
        print("")
    elif choiceReturn == 3: # Dig out of the Prison
        print("")

elif choiceReturn == 2: # Wait Until Nightfall
    print("")
else:
    exit("Something Went Wrong.")