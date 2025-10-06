l = input().split()
k = (len(l[len(l) - 1]) + 1) % 2
l.remove(l[len(l) - 1])
if len(l) % 2 == 0:
    print(bool(k))
elif len(l) % 2 == 1:
    print(not bool(k))
