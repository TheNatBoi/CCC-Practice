q = input()
p = q[-1]
q = q[:-1]
f = q.split(",")
l = f[0].strip()
r = f[1].strip()
o = [r,l]
o = " ".join(o)
o = ((o.lower()).strip()).capitalize()
print(o + p)
