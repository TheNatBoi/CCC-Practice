row1 = ["q","w","e","r","t","y","u","i","o","p"]
row2 = ["a","s","d","f","g","h","j","k","l"]
row3 = ["z","x","c","v","b","n","m"]
t = 0
for _ in range(int(input())):
    s = input()
    c = 0
    for i in range(0, len(s)):
        if s[0] in row1:
            if s[i] in row1:
                c += 1
        elif s[0] in row2:
            if s[i] in row2:
                c += 1
        elif s[0] in row3:
            if s[i] in row3:
                c += 1
    if c == len(s):
        t += 1
print(t)