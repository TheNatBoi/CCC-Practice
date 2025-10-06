s = 0
for _ in range(int(input())):
    l = list(input())
    for i in l:
        if i == "A":
            s += 4
        elif i == "K":
            s += 3
        elif i == "Q":
            s += 2
        elif i == "J":
            s += 1
print(s)