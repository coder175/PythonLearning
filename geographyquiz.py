import time
import fontstyle
import random
import difflib
import re

d = difflib
f = fontstyle
t = time
r = random


def loading():
    randomTicks = random.choice([1, 2, 3])
    for x in range(1, (3 + randomTicks) + 1):
        if x % 3 == 0:
            print(f.apply("■", "bold"), end=" ")
            t.sleep(0.5)
            print("\b \b \b" * 7, end="")
        elif x % 3 == 1:
            t.sleep(0.5)
            print(" ", end="")
            print(f.apply("■", "bold"), end=" ")
            t.sleep(0.25)
        else:
            print(f.apply("■", "bold"), end=" ")
            t.sleep(0.25)
    print("\b", end=" ")
    print("", end="\r")
    DID NOT FINISH


loading()
print(f.apply(' Welcome to the Geography Quiz!', "bold green green_bg"))  # Questions At the Begenning
print("‎ ")
t.sleep(1)
wantInstr = input(
    f.apply("Would you like to read the Instructions? Please type", "green") + f.apply(" Yes", "bold green") + f.apply(
        " or ", "green") + f.apply("No. ", "bold green"))
wantInstr.replace(" ", "")
while wantInstr.lower() not in ("yes", "no", "y", "n"):
    wantInstr = input(f.apply("You typed '" + wantInstr + "'. Please type either Yes or No to skip the instructions.",
                              "bold yellow yellow_bg"))

if wantInstr.lower() in ("yes", "y"):
    t.sleep(0.8)
    print(f.apply("Okay! Here are the instructions for this Quiz:", "green bold"))
    t.sleep(1.5)
    print('You will be asked questions to earn Points. Some questions are:\n')
    t.sleep(1.5)
    print(f.apply('    "What is the capital of Canada?"', "italic"))
    t.sleep(1.5)
    print(f.apply('    "Where is the Taj Mahal Located?"\n', "italic"))
    t.sleep(1.5)
    print('The answer for those two questions are:\n')
    t.sleep(1.5)
    print(f.apply('    "Ottawa" ', "italic"))
    t.sleep(1.5)
    print(f.apply('    "India"\n  ', "italic"))
    t.sleep(1.5)
    print("You are allowed to CAPATALIZE your answer.")
    t.sleep(1.5)
    print("When you're giving the place of a important location, put the country, not the city or state.\n ")
    t.sleep(1.5)
    print("The answer will be correct if it's higher than 85%, and it'll be partially right if it's "
          "higher than 65%")
    t.sleep(1.5)
    print('You can have 1 redemption questions at the end of the quiz for when you get something wrong.')
    t.sleep(1.5)
    print(
        'Every right answer gets 4 points, and every partially right answer gets 2 points. You will get 1 point from a '
        'redeption question.')
    t.sleep(1.5)
    print('You will have 10 questions, and I will tell how many points you have along the way.')
    t.sleep(1.5)
    print("You can get a hint by typing '" + f.apply(" h ", "bold red red_bg") + "'!")
    print(f.apply(' Good Luck! ', "bold green green_bg"))
    t.sleep(1.5)
    print("")
else:
    t.sleep(0.8)
    print(f.apply("Okay! Skipping the Instructions.", "bold green"))
    t.sleep(1)
# All of the questions that are in the Quiz
questions = {
    "What is the Capital of Argentina?": "Buenos Aires",
    "What is the Capital of Australia?": "Canberra",
    "What is the Capital of Brazil?": "Brasilia",
    "What is the Capital of Canada?": "Ottawa",
    "What is the Capital of China?": "Beijing",
    "What is the Capital of Egypt?": "Cairo",
    "What is the Capital of France?": "Paris",
    "What is the Capital of Germany?": "Berlin",
    "What is the Capital of India?": "New Delhi",
    "What is the Capital of Indonesia?": "Jakarta",
    "What is the Capital of Iran?": "Tehran",
    "What is the Capital of Italy?": "Rome",
    "What is the Capital of Japan?": "Tokyo",
    "What is the Capital of Mexico?": "Mexico City",
    "What is the Capital of Netherlands?": "Amsterdam",
    "What is the Capital of Nigeria?": "Abuja",
    "What is the Capital of Pakistan?": "Islamabad",
    "What is the Capital of Philippines?": "Manila",
    "What is the Capital of Poland?": "Warsaw",
    "What is the Capital of Russia?": "Moscow",
    "What is the Capital of Saudi Arabia?": "Riyadh",
    "What is the Capital of South Africa?": "Cape Town",
    "What is the Capital of South Korea?": "Seoul",
    "What is the Capital of Spain?": "Madrid",
    "What is the Capital of Sweden?": "Stockholm",
    "What is the Capital of Thailand?": "Bangkok",
    "What is the Capital of Turkey?": "Ankara",
    "What is the Capital of United Kingdom?": "London",
    "What is the Capital of United States?": "Washington, D.C.",
    "What is the Capital of Vietnam?": "Hanoi",
    "Where is the Taj Mahal located?": "India",
    "Where is the Eiffel Tower located?": "France",
    "Where is the Great Wall of China located?": "China",
    "Where is the Statue of Liberty located?": "United States",
    "Where is Machu Picchu located?": "Peru",
    "Where is the Pyramids of Giza located?": "Egypt",
    "Where is the Colosseum located?": "Italy",
    "Where is the Petra located?": "Jordan",
    "Where is the Christ the Redeemer located?": "Brazil",
    "Where is the Sydney Opera House located?": "Australia",
    "Where is the Acropolis of Athens located?": "Greece",
    "Where is the Sagrada Familia located?": "Spain",
    "Where is the Burj Khalifa located?": "United Arab Emirates",
    "Where is Mount Rushmore located?": "United States",
    "Where is the Kremlin located?": "Russia",
    "Where is the Neuschwanstein Castle located?": "Germany",
    "Where is Chichen Itza located?": "Mexico",
    "Where are the Moai Statues of Easter Island located (Which country owns it)?": "Chile",
    "What is the Longest River in the World (Just put the name of the river)?": "Nile",
    "Which CONTINENT has the Sahara Desert?": "Africa",
    "What COUNTRY has the Golden Gate Bridge?": "United States",
    "Which COUNTRY contains most of the Amazon Rainforest?": "Brazil",
    "What COUNTRY is the Great Barrier Reef next to?": "Australia",
    "What COUNTRY is Mount Everest located in?": "Nepal",
    "What CONTINENT is the Nile River located in?": "Africa",
    "What COUNTRY is the Eiffel Tower located in?": "France",
    "What COUNTRY is the Colosseum located in?": "Italy",
    "What COUNTRY is the Kremlin located in?": "Russia",
    "What COUNTRY is the Grand Canyon located in?": "United States",
    "What COUNTRY is the Great Wall of _____ located in?": "China",
    "What COUNTRY is the Statue of Liberty located in?": "United States",
    "What COUNTRY is the Taj Mahal located in?": "India",
    "What COUNTRY is the Sydney Opera House located in?": "Australia",
    "What COUNTRY is the Acropolis located in?": "Greece",
    "What COUNTRY is the Machu Picchu located in?": "Peru",
    "What COUNTRY is the Mount Kilimanjaro located in?": "Tanzania",
    "What COUNTRY is the Angkor Wat located in?": "Cambodia",
    "What COUNTRY is the Christ the Redeemer located in?": "Brazil"
}

numbers = {
    0: "FIRST",
    1: "SECOND",
    2: "THIRD",
    3: "FOURTH",
    4: "FIFTH",
    5: "SIXTH",
    6: "SEVENTH",
    7: "EIGHTH",
    8: "NINTH",
    9: "TENTH",
}

correct = 0.0
points = 0
grades = []
incorrectQ = []
usedQ = []

for nth in range(2):
    print("\n")
    loading()
    print('Here is your ' + f.apply(" " + numbers[nth] + " ", "bold green green_bg") + ' Question:')
    t.sleep(0.8)
    availableQ = list(set(questions.keys()) - set(usedQ))
    randIndex = random.randint(0, len(availableQ) - 1)
    Q = availableQ[randIndex]
    answer = questions[Q]
    t.sleep(0.5)
    userAns = input(Q + " ")
    print("")
    userAns = re.sub(r"[^a-zA-Z]", "", userAns.lower())
    # Find % Similar:
    similar = d.SequenceMatcher(None, re.sub(r"[^a-zA-Z]", "", answer.lower()), userAns)
    percentSimilar = similar.ratio() * 100
    grades.append(percentSimilar)
    loading()
    if percentSimilar >= 85.0:
        print(f.apply(" Correct!", "bold green"))
        t.sleep(1.5)
        if percentSimilar != 100.0:
            print("Answer: " + answer + ".")
            t.sleep(0.8)
        print("Accuracy: " + f.apply(str(int(percentSimilar)), "bold green"))
        correct += 1.0
        points += 4
    elif percentSimilar <= 65.0:
        print(f.apply("Incorrect.", "red bold"))
        t.sleep(0.8)
        print("Answer: " + answer + ".")
        t.sleep(0.8)
        print("Accuracy: " + f.apply(str(int(percentSimilar)), "bold red"))
        incorrectQ.append(Q)
    else:
        print(f.apply("Partially Correct!", "bold yellow"))
        t.sleep(1.5)
        print("Answer: " + answer + ".")
        t.sleep(1.5)
        print("Accuracy:" + f.apply(str(int(percentSimilar)), "bold yellow"))
        correct += 0.5
        points += 2
    t.sleep(1)
    print("")
    t.sleep(0.5)
    print("")
    print(f"Total Questions Correct: {correct}")
    t.sleep(0.7)
    print(f"Total Points: {points}")
    t.sleep(0.7)
    print(f"Total Average: {int((sum(grades)) / len(grades))}%")
    t.sleep(1.2)

    usedQ.append(Q)
print("")
t.sleep(0.75)
print("These are you results: ")
print("")
print(f.apply(f" Total Questions Correct: {correct} ", "bold red red_bg"))
t.sleep(0.7)
print(f.apply(f" Total Points: {points} ", "bold red red_bg"))
t.sleep(0.7)
print(f.apply(f" Total Average: {int((sum(grades)) / len(grades))}% ", "bold red red_bg"))
t.sleep(1.2)

if len(incorrectQ) > 0:
    print("Time for you Redemption Question!")
    t.sleep(0.5)
    randomInncorectQ = random.choice(incorrectQ)
    redemptionAnswer = questions[randomInncorectQ]
    print("")
    print("Here it is:")
    userRedemptionAns = input(randomInncorectQ + " ")
    print("")
    userAns = re.sub(r"[^a-zA-Z]", "", userRedemptionAns.lower())
    # Find % Similar:
    redemptionSimilar = d.SequenceMatcher(None, re.sub(r"[^a-zA-Z]", "", redemptionAnswer.lower()), userAns)
    percentSimilar = redemptionSimilar.ratio() * 100
    loading()
    print(percentSimilar)
# Add More Questions
