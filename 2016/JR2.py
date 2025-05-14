line1 = input()
line2 = input()
line3 = input()
line4 = input()
lines = [line1, line2, line3, line4]
initColCounter = 0
initRowCounter = 0
colCounter = 0
rowCounter = 0

for i in range(4):
    lines[i] = lines[i].split(" ")
    initColCounter += int(lines[i][0])
    initRowCounter += int(lines[0][i])
for j in range(4):
    for k in range(4):
        colCounter += int(lines[k][j])
    for l in range(4):
        rowCounter += int(lines[j][l])
if (rowCounter == (4 * initRowCounter)) & (colCounter == (4 * initColCounter)):
    print("magic")
else:
    print("not magic")