import itertools
import time
import random
num = ("0123456789")
amount = input('How many digits do you want the secret password to be? ')
while not amount.isdigit():
    print('Please Give a number')
    amount = input('How many digits do you want the secret password to be? ')
amount = int(amount)
password = ''
for x in range(amount):
    password = password + str(random.randint(0, 9))
print(password)
start = time.time()
counter = 1
charNum = 1

#This stops the program once it gets to 25 chars (most people would run out of patience WAY before that
#But if you feel the need you can increase the number.
for charNum in range(25):
    passwords = (itertools.product(num, repeat = charNum))
    print("\n \n")
    print("currently working on passwords with ", charNum, " chars")
    print("It has been ", "{:,}".format(round(time.time() - start)), " seconds!")
    print("We have tried ", "{:,}".format(counter), " possible passwords!")
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
            timetaken = end - start
            print('\n \n')
            print('I used ' + "{:,}".format(counter) + ' tries.')
            print('I used ' + "{:,}".format(end) + ' seconds to find the password.')
            print('Also the password is ' + "{:,}".format(int(i)))
            exit()