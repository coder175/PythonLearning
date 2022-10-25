num = input('How many fibonacci numbers do you want to show? ')
while not num.isdigit():
    print('Please use a number')
    num = input('How many fibonacci numbers do you want to show? ')
num = int(num)
num -= 1
n1, n2 = 0, 1
print(str(n1) + ', ', end='')
print(str(n2) + ', ', end='')
while num > 1:
    swichBox = n1 + n2
    print(str(swichBox) + ', ', end='')
    n1 = n2
    n2 = swichBox
    num -= 1
