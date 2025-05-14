i = int(input())
direction = ""
while int(i) != 99999:
    d = list(str(i))
    if (int(d[0]) + int(d[1])) % 2 == 1:
        direction = "left"
    elif (int(d[0]) + int(d[1])) == 0:
        pass
    else:
        direction = "right"
    steps = int(d[2]) * 100 + int(d[3]) * 10 + int(d[4])
    print(direction, steps)
    i = input()