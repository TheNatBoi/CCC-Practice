N = int(input())
s = []
l = []
for i in range(N):
    s.append(input())
j = 0
count = 0
while j < len(s):
    k = 0
    while k < len(s):
        if s[j] == s[k] and j != k:
            l.append(s[j])
        k+=1
    j+=1
m = 0
while m < len(s):
    n = 0
    while n < len(l):
        if l[n] == s[m]:
            s.remove(s[m])
        n+=1
    m+=1
print(len(s))