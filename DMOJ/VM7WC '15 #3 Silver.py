l = input().split()
s = []
for _ in range(int(l[0])):
    s.append(int(input()))
s.sort()
s.reverse()
tot = 0
for j in range(int(l[1])):
    if s[j] > 0: tot += s[j]
print(tot)