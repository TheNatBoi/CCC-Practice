q = list(map(int, input().split(" ")))
N = q[0]
M = q[1]
doors = 0
d1 = int(input())
for _ in range(M-1):
    d2 = int(input())
    if d2 - 1 == d1 or d2 + 1 == d1:
        doors += 1
    else:
        doors += 2
    d1 = d2
print(doors + 2)