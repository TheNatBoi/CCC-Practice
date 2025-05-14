n = int(input())
for i in range(n):
    l = list(input())
    print(l)
    for j in range(1, len(l)):
        if l[j-1] == l[j]:
            del l[j]
            j-=1
    print(l)