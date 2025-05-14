tot = 0
diff = 100
diffs = []
for _ in range(10):
    tot += int(input())
    diff = 100 - tot
    diffs.append(int(diff))
minimum = 100
posdifs = diffs
posdifs = list(map(abs, posdifs))
index = 0
for i in range(len(posdifs)):
    if posdifs[i] <= minimum:
        minimum = posdifs[i]
        index = i
minimum = diffs[index]
print(100 - minimum)