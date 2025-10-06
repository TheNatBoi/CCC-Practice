from math import ceil

l = input().split(" ")
N = int(l[0])
B = int(l[1])
S = int(l[2])
G = int(l[3])
score = B + S * 3 + G * 5
diff = abs(score - N)
if diff == 0:
    print(1)
else:
    print(ceil(diff/5))
# can't figure out what's wrong