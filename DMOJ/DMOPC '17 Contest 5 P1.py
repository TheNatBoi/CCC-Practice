s = list(input())
for i in range(len(s)):
    if s[i] == '0':
        s[i] = "O"
    elif s[i] == '1':
        s[i] = "l"
    elif s[i] == '3':
        s[i] = "E"
    elif s[i] == '4':
        s[i] = "A"
    elif s[i] == '5':
        s[i] = "S"
    elif s[i] == '6':
        s[i] = "G"
    elif s[i] == '8':
        s[i] = "B"
    elif s[i] == '9':
        s[i] = "g"

print("".join(s))