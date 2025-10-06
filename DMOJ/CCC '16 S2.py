q = int(input())
input()
d = list(map(int, input().split()))
p = list(map(int, input().split()))
s = 0
if q == 1:
    while len(d) != 0:
        s += max(max(d),max(p))
        d.remove(max(d))
        p.remove(max(p))
    print(s)
else:
    while len(d) != 0:
        s += max(max(d),min(p))
        d.remove(max(d))
        p.remove(min(p))
    print(s)