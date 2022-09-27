numbers = input('What are your numbers? Separate them with a comma. ')
numbers = numbers.split(',')
numbers = [float(y) for y in numbers]
i = 0
for x in numbers:
    i = i + x
i = i / len(numbers)
print(i)
