from math import sqrt

w = input().split(" ")
x1 = int(w[0])
y1 = int(w[1])
w = input().split(" ")
x2 = int(w[0])
y2 = int(w[1])
w = input().split(" ")
xs = int(w[0])
ys = int(w[1])
D = int(input())
dist1 = sqrt((xs-x1) ** 2 + (ys-y1) ** 2)
dist2 = sqrt((xs-x2) ** 2 + (ys-y2) ** 2)
if dist1 <= D or dist2 <= D:
    print("Yes")
else:
    print("No")