q = input().split(" ")
a = [q[0]]
q = int(q[1])
for _ in range(q):
    w = input().split(" ")
    o = w[0]
    if o == "C":
        a.append(a[int(w[1])-1] + w[2])
        # print(a)
    if o == "Q":
        p = w[1]
        c = 0
        for j in range(len(a)):
            if p in a[j]:
                print(j+1)
                break
            elif p not in a[j]:
                c+=1
            if c == len(a):
                for k in range(len(p)-1, 1, -1):
                    r = 0
                    if p[:k] in a[j]:
                        print(j)
                        break
                    else:
                        r+=1
                    if r == len(a):
                        print(-1)

        # gave up