n = int(input())
coords = input()
split = coords.split(',')
x = int(split[0])
y = int(split[1])
minx = x-1
miny = y-1
maxx = x+1
maxy = y+1
for i in range(n-1):
    coords = input()
    split = coords.split(',')
    x = int(split[0])
    y = int(split[1])
    if x < minx:
        minx = x-1
    if y < miny:
        miny = y-1
    if x > maxx:
        maxx = x+1
    if y > maxy:
        maxy = y+1
print(str(minx) + ',' + str(miny))
print(str(maxx) + ',' + str(maxy))