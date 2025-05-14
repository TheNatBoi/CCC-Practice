w = input().split(" ")
y = int(w[0])
u = int(w[1])
i = int(w[2])
f = [y,u,i]
p1 = max(f)
f.remove(p1)
p2 = int(f[0])
p3 = int(f[1])
if int(p1) < p2 + p3:
    print("yes")
else:
    print("no")