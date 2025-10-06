t1 = int(input())
t2 = int(input())
i = 0
while t2 < t1:
    tn = t1 - t2
    t1 = t2
    t2 = tn
    i += 1
print(i+2)
