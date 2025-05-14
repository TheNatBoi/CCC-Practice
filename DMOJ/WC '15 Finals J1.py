s = list(input())
o = str()

for i in range(len(s)):
    o += s[i] + " "
print(o)
for i in range(len(s)-1):
    print(s[i+1])