w = input().split(" ")
m = int(w[0])/int(w[1])
for _ in range(int(input())):
    j = input().split(" ")
    k = int(j[0])/int(j[1])
    if m > k:
        m = k
print("%.2f" % (m * 1000))