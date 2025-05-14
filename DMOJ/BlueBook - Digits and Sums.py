w = input().split(" ")
l = int(w[0])
u = int(w[1])

for i in range(l, u):
    d = 0
    for j in list(str(i)):
        d += pow(int(j),3)
    if d == i:
        print(i)