w = input().split(" ")
N = int(w[0])
M = int(w[1])
E = int(w[2])
currentHeight = 0
leapsLeft = E
rocksClimbed = 0
for i in range(N):
    nextRock = int(input())
    