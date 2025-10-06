l = []
f = int(input())
while f != -1:
    l.append(f)
    f = int(input())
k = []
for _ in range(len(l)):
    k.append(0)
d = dict(zip(l,k))
for i in range(len(l)):
    if l[i] in d.keys():
        d[l[i]] += 1
o = []
for i in d:
    if d[i] == max(d.values()):
        o.append(i)
o.sort()
for i in o:
    print(i)