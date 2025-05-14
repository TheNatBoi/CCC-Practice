w = input().split(" ")
w = list(map(int, w))
w.sort()
d = {"A": w[0], "B": w[1], "C": w[2]}
g = list(input())
x = ""
for i in range(len(g)):
    x += str(d[g[i]]) + " "
print(x.strip())