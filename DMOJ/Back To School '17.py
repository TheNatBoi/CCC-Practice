h = int(input())
w = []
c = []
for i in range(h):
    w.append(input().split(" "))

for j in range(len(w)):
    c.append((float(w[j][1])-float(w[j][0]))/float(w[j][1]))

t = 1
for k in range(len(c)):
    t *= c[k]

print(t)