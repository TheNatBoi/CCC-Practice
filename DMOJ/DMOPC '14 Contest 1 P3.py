I = int(input())
g = []
for i in range(I):
    g.append(int(input()))
l = sum(g)
for j in range(int(input())):
    f = int(input())
    g.append(f)
    l += f
    out = l/len(g)
    print("%.3f" % out)