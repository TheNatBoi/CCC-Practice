l = list(map(int, input().split()))
N = l[0]
M = l[1]
a = []
for _ in range(N):
    a.append(list(map(int, input().split())))
s = sorted(a, key=lambda x: x[0])
c = 0
t = 0
# while M >= t:
#     if s[0][1] > (M-t):
#         c += (M-t) * s[0][0]
#     else:
#         c += s[0][1] * s[0][0]
#         t += s[0][1]
#     print(s,"\n",c,"\n",t,"\n\n")
#     s.pop(0)
for k in s:
    if k[1] > (M-t):
        c += (M-t) * k[0]
        break
    else:
        c += k[1] * k[0]
        t += k[1]
    if t == M:
        break
print(c)