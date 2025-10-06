l = input().split("x")
l.sort()
print("x".join(l))
k = 1
for i in l:
    k *= int(i)
print(k)