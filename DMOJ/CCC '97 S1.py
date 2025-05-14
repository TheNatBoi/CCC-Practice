n = int(input())

for i in range(n):
    s = int(input())
    v = int(input())
    o = int(input())
    S = []
    V = []
    O = []
    for j in range(s):
        S.append(input())
    for j in range(v):
        V.append(input())
    for j in range(o):
        O.append(input())
    for k in range(len(S)):
        for l in range(len(V)):
            for m in range(len(O)):
                print(S[k] + " " + V[l] + " " + O[m] + ".")