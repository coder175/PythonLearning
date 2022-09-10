def solution(string):
    if string == None or len(string) <= 0: return
    string = string.upper()
    numerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = numerals.get(string[-1])
    for idx in range(len(string) - 2, -1, -1):
            if numerals.get(string[idx]) < numerals.get(string[idx + 1]):
                result -= numerals.get(string[idx])
            else:
                result += numerals.get(string[idx])
    return result
print(solution('XXIV'))
print(solution('XXVI'))