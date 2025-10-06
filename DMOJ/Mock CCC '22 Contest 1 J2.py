l = list(map(int, input().split()))
s = l[1]
l = list(input())
for i in l:
    if i == "D":
        s += 1
    elif i == "U" and s > 1:
        s -= 1
