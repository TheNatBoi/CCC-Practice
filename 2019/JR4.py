def arrToPrint():
    for i in range(2):
        for j in range (2):
            num = grid[i][j]
            print(num, end=' ')
        print("")
line1 = [1,2]
line2 = [3,4]
grid = [line1,line2]
input = list(input())
for i in range(len(input)):
    if input[i] == "H":
        grid.append(grid[0])
        del grid[0]
    elif input[i] == "V":
        line1.append(line1[0])
        del line1[0]
        line2.append(line2[0])
        del line2[0]
arrToPrint()        