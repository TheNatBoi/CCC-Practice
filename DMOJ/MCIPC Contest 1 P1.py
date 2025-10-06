from math import sqrt

l = input().split()
A = int(l[0])
B = int(l[1])

i = (A + sqrt(A ** 2 - 4 * B))/2
ii = (A - sqrt(A ** 2 - 4 * B))/2
C = int(min(i, ii))
D = int(max(i, ii))
print(C,D)