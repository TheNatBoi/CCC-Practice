w = list(input())
l=0
r=0
for x in w:
    if x == "(":
        l+=1
    else:
        r+=1
if abs(l-r) == 2:
    print("YES")
else:
    print("NO")
#gave up