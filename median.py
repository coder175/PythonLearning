import math


def medianCode(num):
    num.sort()
    if(len(num) % 2 == 1):
        pos = math.floor(len(num) / 2)
        return num[pos]
    else:
        pos = math.floor(len(num) / 2)
        return(num[pos - 1] + num[pos]) / 2


print(medianCode([78, 25, 57, 898]))