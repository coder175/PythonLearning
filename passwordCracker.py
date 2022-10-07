import itertools, time, random, os
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


def passCrackOdd():
    global charNum
    for charNum in range(1,25,2):
        passwords = (itertools.product(num, repeat=charNum))
        for i in passwords:
            global counter
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
                os._exit(0)
def passCrackEven():
    global charNum
    for charNum in range(0, 25, 2):
        passwords = (itertools.product(num, repeat=charNum))
        for i in passwords:
            global counter
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
                os._exit(0)


if __name__ == '__main__':
    Thread(target=updateProg).start()
    Thread(target=passCrackOdd).start()
    Thread(target=passCrackEven).start()
