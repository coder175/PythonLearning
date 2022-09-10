numberCount = input('How many fibonacci numbers do you want to show? ')
while not numberCount.isdigit():
    print('Please use a number')
    numberCount = input('How many fibonacci numbers do you want to show? ')
numberCount = int(numberCount)
numberCount -= 1
firstBox = 0
secondBox = 1
print(str(firstBox) + (', '))
print(str(secondBox) + (', '))
while (numberCount > 1):
    swichBox = firstBox + secondBox
    print(str(swichBox) + (', '))
    firstBox = secondBox
    secondBox = swichBox
    numberCount -= 1