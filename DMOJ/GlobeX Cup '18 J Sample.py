l = input().split()
N = int(l[0])
M = int(l[1])
f = sorted(list(map(int, input().split())))
tot = 0
for i in range(M):
    f.remove(f[0])
for i in f:
    tot += i
print(tot)