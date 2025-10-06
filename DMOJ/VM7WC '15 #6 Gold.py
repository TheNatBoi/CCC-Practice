t = int(input())
l = []
slaves = []
for _ in range(t-1):
    l.append(list(map(int,input().split())))
chars = list(map(int,input().split()))
# print(l, "\n", chars)
for i in range(len(l)):
    slaves.append(l[i][0])
# print(l, "\n", chars, slaves)
for i in range(len(slaves)):
    pass
# too much effort