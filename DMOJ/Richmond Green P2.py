x = []
y = []
for _ in range(int(input())):
    w = input().split(" ")
    x.append(int(w[0]))
    y.append(int(w[1]))
print((max(x) - min(x)) * (max(y) - min(y)))