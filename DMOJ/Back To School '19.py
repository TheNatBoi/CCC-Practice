q = int(input())
l = input().split(" ")
s = input()
m = 0
for i in range(len(l)):
    if m < len(l[i]) <= len(s):
        m = len(l[i])
        c = l[i]
print(c)