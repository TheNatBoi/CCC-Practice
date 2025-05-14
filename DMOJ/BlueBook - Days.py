T = int(input())
for i in range(T):
    N = list(input().split(' '))
    y = int(N[0])
    m = int(N[1])
    d = int(N[2])
    if m == 1:
        count = d
    elif m == 2:
        count = d + 31
    elif m == 3:
        count = d + 28 + 31
    elif m == 4:
        count = d + 28 + 31 * 2
    elif m == 5:
        count = d + 28 + 31 * 2 + 30
    elif m == 6:
        count = d + 28 + 31 * 3 + 30
    elif m == 7:
        count = d + 28 + 31 * 3 + 30 * 2
    elif m == 8:
        count = d + 28 + 31 * 4 + 30 * 2
    elif m == 9:
        count = d + 28 + 31 * 5 + 30 * 2
    elif m == 10:
        count = d + 28 + 31 * 5 + 30 * 3
    elif m == 11:
        count = d + 28 + 31 * 6 + 30 * 3
    elif m == 12:
        count = d + 28 + 31 * 6 + 30 * 4
    if y % 4 == 0:
        count += 1
    print(count)