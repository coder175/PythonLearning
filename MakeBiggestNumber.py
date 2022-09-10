print('Input numbers until you feel like you want to stop. To stop, input e.')
number = ''
while True:
    userInput = input('Enter Your first Number or input e to stop. ')
    userInput = userInput.lower()
    print('YOUR INPUT IS   ' + type(userInput))
    if userInput == 'e':
        break
    else:
        while not userInput.isdigit() or not userInput == 'e':
            print('Your Input you entered is Invalid, Only numbers and the letter e are allowed. ')
            userInput = input('Reenter Your first Number or input e to stop. ')

number = list(number)
sortedNumber = sorted(number, reverse=True)
answer = ''.join(sortedNumber)
print("{:,}".format(int(answer)))