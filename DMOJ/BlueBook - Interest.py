l = list(map(float, input().split()))
p = l[0]
r = l[1]
n = int(l[2])
for i in range(n+1):
    print(str(i) + " " + "{:.2f}".format(p))
    p = p * (1 + r/100)