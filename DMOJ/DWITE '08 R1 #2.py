ab = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for _ in range(5):
    w = input().split(" ")
    l = w[1]
    d = list(w[0])
    tot = 0
    while int("".join(d))//10 != 0:
        for i in d:
            tot += int(i)
        d = list(str(tot))
        tot = 0
    if ab[int(d[0])-1] == l:
        print("match")
    else:
        print("error")