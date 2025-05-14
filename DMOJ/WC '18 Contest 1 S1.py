q = input().split(" ")
R = int(q[0])
C = int(q[1])
K = int(q[2])
grid = []
c = 0

for _ in range(R):
    w = input().split(" ")
    grid.append(w)

for row in range(len(grid)):
    for col in range(row):
        if grid[row][col] == "2":
            for i in range(K):
                if grid[row - i][col] == 1:
                    c += 1
                    break