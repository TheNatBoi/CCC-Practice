names = []
bids = []
for _ in range(int(input())):
    names.append(input())
    bids.append(int(input()))
maxi = 0
index = 0
for i in range(len(bids)):
    if maxi < bids[i]:
        maxi = bids[i]
        index = i
print(names[index])