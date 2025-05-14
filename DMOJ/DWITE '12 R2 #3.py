def s(k):
    if k == 0 or k == 1 or k == 2:
        return 1
    else:
        return s(k-2) + s(k-3)
for _ in range(5):
    print(s(int(input())))