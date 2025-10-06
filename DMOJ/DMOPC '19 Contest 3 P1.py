k = input()
l = map(int, input().split())
d = {}

for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
m = 0
j = []
for i in d:
    if d[i] >= m:
        m = d[i]
        j.append(str(i))
j.sort()
print((", ".join(j)))