f = input().split(" ")
N = int(f[0])
Q = int(f[1])
l = []

for i in range(N):
    p = input().split(" ")
    P = int(p[0])
    O = int(p[1])
    l.append(range(P,O+1))
for j in range(Q):
    g = int(input())
    count = 0
    for k in l:
        if g in k:
            count+=1
    print(count)