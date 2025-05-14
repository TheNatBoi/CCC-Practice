a = int(input())
while a >= 0:
    print("Account #: " + str(a))
    b = input().split(" ")
    s = int(b[0])
    e = int(b[1])
    f = e-s
    if f < 0:
        n = ""
        for _ in range(len(str(s))):
            n += "9"
        f = int(n) - s + e + 1
    if f <= 10:
        print("Bill: 6.59")
    elif f <= 30:
        print("Bill: " + str("%.2f" % (0.2373 * (f-10) + 6.59)))
    elif f <= 85:
        print("Bill: " + str("%.2f" % (0.2271 * (f-30) + 4.746 + 6.59)))
    elif f <= 170:
        print("Bill: " + str("%.2f" % (0.2178 * (f-85) + 12.4905 + 4.746 + 6.59)))
    else:
        print("Bill: " + str("%.2f" % (0.2085 * (f-170) + 18.513 + 12.4905 + 4.746 + 6.59)))
    a = int(input())