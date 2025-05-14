output = ''
prevDir = ''
outlist = []

while True:
    i = input()
    if int(i) == 99999:
        break
    inlist = list(i)
    if (((int(inlist[0]) + int(inlist[1])) % 2 == 0) & ((int(inlist[0]) + int(inlist[1])) != 0)):
        output = 'right '
        prevDir = 'right'
    elif ((int(inlist[0]) + int(inlist[1])) % 2 == 1):
        output = 'left '
        prevDir = 'left'
    elif (int(inlist[0]) + int(inlist[1]) == 0):
        output = prevDir + ' '
    outlist.append(str(output + str(int(inlist[2])*100 + int(inlist[3])*10 + int(inlist[4]))))
for i in range(len(outlist)):
    print(outlist[i])
