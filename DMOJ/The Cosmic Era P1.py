arr = ["B","F","T","L","C"]
B = 0
F = 0
T = 0
L = 0
C = 0
t = list(input())
for i in range(len(t)):
    if t[i] == arr[0]:
        B = 1
    elif t[i] == arr[1]:
        F = 1
    elif t[i] == arr[2]:
        T = 1
    elif t[i] == arr[3]:
        L = 1
    elif t[i] == arr[4]:
        C = 1
if B == 1 and F == 1 and T == 1 and L == 1 and C == 1:
    print("NO MISSING PARTS")
else:
    s = ""
    if B == 0:
        s += "B"
    if F == 0:
        s += "F"
    if T == 0:
        s += "T"
    if L == 0:
        s += "L"
    if C == 0:
        s += "C"
    print(s)