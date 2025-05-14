N, T = map(int, input().split(" "))
count = 0
for i in range(N):
    c, d = map(int, input().split(" "))
    if c * (100-d) * 0.01 <= T:
        count += 1
print(count)