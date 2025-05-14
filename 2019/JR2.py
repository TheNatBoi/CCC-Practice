lines = int(input())
for i in range(lines):
    line = str(input())
    split = line.split(' ')
    r = int(split[0])
    c = str(split[1])
    printline = []
    for j in range(r):
        print(c, end='')