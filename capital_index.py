# original
def capital_indexes(str):
    cap = []
    for index, letter in enumerate(str):
        if letter.isupper():
            cap.append(index)
    return cap
        
print(capital_indexes('HeLlO'))

# naive solution
def capital_indexes(s):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i, l in enumerate(s):
        if l in upper:
            result.append(i)
    return result

# shorter version
from string import uppercase
def capital_indexes(s):
    return [i for i in range(len(s)) if s[i] in uppercase]