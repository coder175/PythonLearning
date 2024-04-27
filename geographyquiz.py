import time
import fontstyle
import random
import difflib

d = difflib
f = fontstyle
t = time
r = random
print(f.apply(' Welcome to the Geography Quiz!', "bold green green_bg"), end="\n")  # Questions At the Begenning
time.sleep(1)
wantInstr = input(f.apply("Would you like to read the Instructions? Please type Yes or No. ", "bold green"))
wantInstr.strip()
while wantInstr.lower() not in ("yes", "no", "y", "n"):
    wantInstr = input(f.apply("You typed '" + wantInstr + "'. Please type either Yes or No to skip the instructions.",
                              "bold yellow yellow_bg"))

if wantInstr.lower() in ("yes", "y"):
    print(f.apply("Okay! Here are the instructions for this Quiz:", "green bold"))
    time.sleep(0.4)
    print('You will be asked questions to earn Points. Some questions are:\n ')
    time.sleep(1)
    print(f.apply('    "What is the capital of Canada?"     ', "italic"))
    time.sleep(1)
    print(f.apply('    "Where is the Taj Mahal Located?"\n   ', "italic"))
    time.sleep(1)
    print('The answer for those two questions are:\n ')
    time.sleep(1)
    print(f.apply('    "Ottawa" ', "italic"))
    time.sleep(1)
    print(f.apply('    "India"\n  ', "italic"))
    time.sleep(1)
    print("You can CAPATALIZE or put symbols (like periods, hyphens, etc.) in your answer, it won't change your "
          "score. ")
    time.sleep(1)
    print("  When you're giving the place of a important location, put the country, not the city or state.\n ")
    time.sleep(1)
    print('If your answer matches 85% or higher than the actual answer, then it will be considered right. If your '
          'answer matches 65% or higher than the actual answer, it will be considered partially right (it will be '
          'counted as half a question correct).')
    time.sleep(3)
    print('You can have 1 redemption question at the end of the quiz if you get something wrong.')
    time.sleep(1)
    print(
        'For every question you get right, you earn 4 points, for every question you get partially right, you earn 2 '
        'points, and for every redemption question you get right, you earn 1 point.')
    time.sleep(1)
    print('You will have 10 questions, and I will tell how many points you have along the way.')
    time.sleep(1)
    print(f.apply(' Good Luck! ', "bold green green_bg"))
    time.sleep(1)
else:
    print("\n")
    time.sleep(0.25)
    print(f.apply("Okay! Skipping the Instructions.", "bold green"))
    time.sleep(1)
print(*['\n'] * 2)  # Print 2 Lines
print(f.apply(" READY?", "bold red red_bg"))
time.sleep(1)
print("\n", end="")
print(f.apply(' GO!', "bold green green_bg"), end="\n")
time.sleep(0.8)
print("\n")
# All of the questions that are in the Quiz
questions = {
    "What is the Capital of Argentina?": "Buenos Aires",
    "What is the Capital of Australia?": "Canberra",
    "What is the Capital of Brazil?": "Brasília",
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
    "Where is the Angkor Wat located?": "Cambodia",
    "Where is the Acropolis of Athens located?": "Greece",
    "Where is Stonehenge located?": "United Kingdom",
    "Where is the Sagrada Familia located?": "Spain",
    "Where is the Burj Khalifa located?": "United Arab Emirates",
    "Where is Mount Rushmore located?": "United States",
    "Where is the Kremlin located?": "Russia",
    "Where is the Neuschwanstein Castle located?": "Germany",
    "Where is Chichen Itza located?": "Mexico",
    "Where are the Moai Statues of Easter Island located? (Which country owns it)": "Chile"
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
incorrectQ = []
usedQ = []

for nth in range(10):
    time.sleep(1)
    print('Here is your ' + f.apply(" " + numbers[nth] + " ", "bold green green_bg") + ' Question:')
    time.sleep(0.8)
    availableQ = list(set(questions.keys()) - set(usedQ))
    randIndex = random.randint(0, len(availableQ) - 1)
    Q = availableQ[randIndex]
    answer = questions[Q]

    userAns = input(Q + " ")
    userAns = userAns.strip().lower()
    # Find % Similar:

    similar = d.SequenceMatcher(None, answer.strip().lower(), userAns)
    percentSimilar = similar.ratio() * 100
    if percentSimilar >= 85.0:
        print("You got it right!")
        time.sleep(0.8)
        if percentSimilar != 100.0:
            print("The answer was " + answer + ".")
            time.sleep(0.8)
        print("You were " + str(int(percentSimilar)) + "% right!")
        time.sleep(0.8)
        print("Your score is higher than 85%, so it's counted right.")
        time.sleep(0.8)
        print("You got 4 points!")
        correct += 1.0
        points += 4
    elif percentSimilar <= 65.0:
        print("You got it wrong.")
        time.sleep(0.8)
        print("The answer was " + answer + ".")
        time.sleep(0.8)
        print("You were " + str(int(percentSimilar)) + "% right, and you were " + str(85 - int(percentSimilar)) +
              "% close to getting it right.")
        time.sleep(1.5)
        print("Your score is lower than 85%, so it was counted wrong.")
        time.sleep(1.2)
        print("You could try and get it right as a Redemption Question.")
    else:
        print("You got the answer partially right!")
        print("The answer was " + answer + ".")
        time.sleep(0.8)
        print("You were {str(int(percentSimilar))}% right.")
        print("You were {str(65 - int(percentSimilar))}% close to getting it partially right, and {str(85 - int("
              "percentSimilar))}% close to getting it right.")
        time.sleep(1.5)
        print("Your score is lower than 85%, so it was counted wrong.")
        time.sleep(1.2)
        print("You could try and get it right as a Redemption Question.")
        correct += 0.5
        points += 2
    print("\n")
    time.sleep(0.8)
    print("You got {correct} questions correct, and you have {points} points!")
# Add More Questions