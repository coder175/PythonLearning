
operation = input('What operation do you want to use? Type in Add, Sub, Multiply, or Divide: ')
operation = operation.lower()
while operation not in ('add', 'sub', 'multiply', 'divide'):
    operation = input('Please Reenter Add, Sub, Multiply, or Divide.')


number1 = input('Enter Your first number: ')
while not str.isdigit(number1):
    print('The Number you have entered in not Numeric. Please enter a valid number: ')
    number1 = input('Enter Your First Valid Number: ')

number2 = input('Enter Your second number: ')
while not str.isdigit(number2):
    print('The Number you have entered in not Numeric. Please enter a valid number: ')
    number2 = input('Enter Your First Valid Number: ')
if operation == 'add':
    print(int(number1) + int(number2))
elif operation == 'sub':
    print(int(number1) - int(number2))
elif operation == 'multiply':
    print(int(number1) * int(number2))
elif operation == 'divide':
    print(int(number1) / int(number2))