for _ in range(5):
    s = ""
    l = list(map(int, input().split()))
    for num in l:
        r = list(str(num))
        r.reverse()
        r = int("".join(r))
        d = 0
        for i in range(0, len(str(r)), 2):
            k = 2 * int(str(r)[i])
            for j in str(k):
                d += int(j)
        for i in range(1, len(str(r)), 2):
            d += int(str(r)[i])
        s += str((10 - (d % 10)) % 10)
    print(s)
    # almost right