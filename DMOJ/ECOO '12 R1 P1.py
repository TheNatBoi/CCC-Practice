title = input()
print(title)
print("====================")
totSa = 0
totBa = 0
for _ in range(10):
    l = input().split()
    name = l[0]
    garbage = l[1]
    E = float(l[2])
    totHits = float(l[4])
    B = float(l[5])
    C = float(l[6])
    D = float(l[7])
    out = str(round(totHits/E, 3))[1:]
    while len(out) < 4:
        out = out + "0"
    A = totHits - B - C - D
    sa = str(round((A + 2 * B + 3 * C + 4 * D) / E, 3))[1:]
    totSa += (A + 2 * B + 3 * C + 4 * D) / E
    totBa += totHits / E
    while len(sa) < 4:
        sa = sa + "0"
    print(name + ": " + out + " " + sa)
print("====================")
print(totBa, totSa)
totBa = str(round(totBa/10, 3))[1:]
totSa = str(round(totSa/10, 3))[1:]
print("Big 10 Av: " + totBa + " " + totSa)
# answer was .267 in top 10 but i get .266