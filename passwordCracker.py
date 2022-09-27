import itertools
import time
import random
from threading import Thread

num = "0123456789"
amount = input('How many digits do you want the secret password to be? ')
while not amount.isdigit():
    print('Please Give a number')
    amount = input('How many digits do you want the secret password to be? ')
amount = int(amount)
password = ''
for x in range(amount):
    password = password + str(random.randint(0, 9))
print(password)
global start, counter, charNum
start = time.time()
charNum = 1
counter = 1


def updateProg():
    starttime = time.time()
    while True:
        print("\n \n")
        print("I am currently working on passwords with ", charNum, " chars")
        print("It has been ", "{:,}".format(round(time.time() - start)), " seconds!")
        print("We have tried ", "{:,}".format(counter), " possible passwords!")
        time.sleep(2.5 - ((time.time() - starttime) % 2.5))


def passCrack():
    for charNum in range(25):
        passwords = (itertools.product(num, repeat=charNum))
        for i in passwords:
            counter += 1
            i = str(i)
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace("'", "")
            i = i.replace(" ", "")
            i = i.replace(",", "")
            i = i.replace("(", "")
            i = i.replace(")", "")
            if i == password:
                end = round(time.time() - start)
                timeTaken = end - start
                print('\n \n')
                print('I used ' + "{:,}".format(counter) + ' tries.')
                print('I used ' + "{:,}".format(end) + ' seconds to find the password.')
                print('Also the password is ' + "{:,}".format(int(i)))
                exit()


if __name__ == '__main__':
    Thread(target=updateProg).start()
    Thread(target=passCrack).start()
