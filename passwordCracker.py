import itertools, os, random, time
from threading import Thread

num = '0123456789'
amount = input('How many digits do you want the secret password to be? ')
while not amount.isdigit():
    for x in ['ERROR', 'eRROR', 'ErROR', 'ERrOR', 'ERRoR', 'ERROr', 'ERROR']:
        time.sleep(0.25)
        print('\r {}'.format(x), end='')
    print()
    print('Character has to have only number(s).')
    amount = input('How many digits do you want the secret password to be? ')
amount = int(amount)
password = ''
for x in range(amount):
    password = password + str(random.randint(0, 9))
time.sleep(0.5)
print("Here is the password we're trying to find:", password)
time.sleep(1)
print('\n')
start = time.time()
charNum1 = 1
charNum2 = 2
charNum3 = 3
charNum4 = 4
charNum5 = 5
charNum6 = 6
counter = 1

keepRunning = True

def updateProg():
    global keepRunning
    startTime = time.time()
    while keepRunning:
        print(charNum1, charNum2, charNum3, charNum4, charNum5, charNum6, 'running Chars; Seconds:',
              '{:,}'.format(round(time.time() - start)), '. Tries:', '{:,}'.format(counter),
              '.', end='')
        time.sleep(0.5)
        print('\r', end=' ')


def passCrack1():
    global charNum1
    for charNum1 in range(1, 25, 6):
        passwords = (itertools.product(num, repeat=charNum1))
        for i in passwords:
            global counter
            counter += 1
            i = str(i)
            i = i.replace('[', '')
            i = i.replace(']', '')
            i = i.replace("'", '')
            i = i.replace(' ', '')
            i = i.replace(',', '')
            i = i.replace('(', '')
            i = i.replace(')', '')
            if i == password:
                complete(i)


def passCrack2():
    global charNum2
    for charNum2 in range(2, 25, 6):
        passwords = (itertools.product(num, repeat=charNum2))
        for i in passwords:
            global counter
            counter += 1
            i = str(i)
            i = i.replace('[', '')
            i = i.replace(']', '')
            i = i.replace("'", '')
            i = i.replace(' ', '')
            i = i.replace(',', '')
            i = i.replace('(', '')
            i = i.replace(')', '')
            if i == password:
                complete(i)


def passCrack3():
    global charNum3
    for charNum3 in range(3, 25, 6):
        passwords = (itertools.product(num, repeat=charNum3))
        for i in passwords:
            global counter
            counter += 1
            i = str(i)
            i = i.replace('[', '')
            i = i.replace(']', '')
            i = i.replace("'", '')
            i = i.replace(' ', '')
            i = i.replace(',', '')
            i = i.replace('(', '')
            i = i.replace(')', '')
            if i == password:
                complete(i)


def passCrack4():
    global charNum4
    for charNum4 in range(4, 25, 6):
        passwords = (itertools.product(num, repeat=charNum4))
        for i in passwords:
            global counter
            counter += 1
            i = str(i)
            i = i.replace('[', '')
            i = i.replace(']', '')
            i = i.replace("'", '')
            i = i.replace(' ', '')
            i = i.replace(',', '')
            i = i.replace('(', '')
            i = i.replace(')', '')
            if i == password:
                complete(i)


def passCrack5():
    global charNum5
    for charNum5 in range(5, 25, 6):
        passwords = (itertools.product(num, repeat=charNum5))
        for i in passwords:
            global counter
            counter += 1
            i = str(i)
            i = i.replace('[', '')
            i = i.replace(']', '')
            i = i.replace("'", '')
            i = i.replace(' ', '')
            i = i.replace(',', '')
            i = i.replace('(', '')
            i = i.replace(')', '')
            if i == password:
                complete(i)


def passCrack6():
    global charNum6
    for charNum6 in range(6, 25, 6):
        passwords = (itertools.product(num, repeat=charNum6))
        for i in passwords:
            global counter
            counter += 1
            i = str(i)
            i = i.replace('[', '')
            i = i.replace(']', '')
            i = i.replace("'", '')
            i = i.replace(' ', '')
            i = i.replace(',', '')
            i = i.replace('(', '')
            i = i.replace(')', '')
            if i == password:
                complete(i)


def complete(i):
    global keepRunning
    end = round(time.time() - start)
    keepRunning = False
    time.sleep(1)
    print("\n \n \n")
    for x in ['FOUND NUMBER', '#OUND NUMBER', 'F#UND NUMBER', 'FO#ND NUMBER', 'FOU#D NUMBER', 'FOUN# NUMBER', 'FOUND#NUMBER', 'FOUND #UMBER', 'FOUND N#MBER', 'FOUND NU#BER', 'FOUND NUM#ER', 'FOUND NUMB#R', 'FOUND NUMBE#', 'FOUND NUMBER']:
        time.sleep(0.1)
        print('\r {}'.format(x), end='')
    print()
    print('Seconds Used:', '{:,}'.format(round(time.time() - start - 2)), '. Tries:', '{:,}'.format(counter), ". Password Found:",
          '{:,}'.format(int(i)))
    os._exit(0)


if __name__ == '__main__':
    Thread(target=updateProg).start()
    Thread(target=passCrack1).start()
    Thread(target=passCrack2).start()
    Thread(target=passCrack3).start()
    Thread(target=passCrack4).start()
    Thread(target=passCrack5).start()
    Thread(target=passCrack6).start()
