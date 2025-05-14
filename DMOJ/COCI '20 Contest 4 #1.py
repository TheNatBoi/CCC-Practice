q = input().split(" ")
q.remove(q[0])
m = int(input())
l = []
for i in range(m):
    u = input().split(" ")
    u.remove(u[0])
    l.append(u)
count = len(l)
for i in l:
    if any(item in q for item in i):
        count -= 1
print(count)