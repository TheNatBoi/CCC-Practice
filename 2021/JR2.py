num = int(input())
bid0:int = 0

for i in range(num):
    name = input()
    bid = int(input())
    if bid > bid0:
        bid0 = bid
        g = name

print(g)