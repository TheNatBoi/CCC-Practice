import string
import re

N = int(input())

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits

for i in range(N):
    sum1 = 0
    newCode = ""
    oldCode = str(input())
    numbers = re.findall(r'-?\d+', oldCode)
    for i in range(len(oldCode)):
        if oldCode[i] in upper:
            newCode += oldCode[i]
        elif oldCode[i] in lower:
            pass
        elif oldCode[i] in digits or oldCode[i] == "-":
            continue
    for number in numbers:
        sum1 += int(number)
    newCode += str(sum1)
    print(newCode)