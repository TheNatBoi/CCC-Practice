grid = [["1","2"],["3","4"]]
ops = list(input())
for i in ops:
    if i == "V":
        temp = grid[0][1]
        grid[0][1] = grid[0][0]
        grid[0][0] = temp
        temp = grid[1][1]
        grid[1][1] = grid[1][0]
        grid[1][0] = temp
    elif i == "H":
        temp = grid[1]
        grid[1] = grid[0]
        grid[0] = temp
out = " ".join(grid[0]) + "\n" + " ".join(grid[1])
print(out)