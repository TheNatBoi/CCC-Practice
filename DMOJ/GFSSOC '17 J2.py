from statistics import mean
l = []
for i in range(6):
    l.append(int(input()))
m = mean(l)
if m + int(input()) >= int(input()): print("yes")
else: print("no")