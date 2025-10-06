from math import ceil

for _ in range(10):
    k = input()
    l = []
    while k != "end of box":
        l.append(k)
        k = input()
    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    for i in range(len(l)):
        if l[i] == "orange":
            c0+=1
        elif l[i] == "blue":
            c1+=1
        elif l[i] == "green":
            c2+=1
        elif l[i] == "yellow":
            c3+=1
        elif l[i] == "pink":
            c4+=1
        elif l[i] == "violet":
            c5+=1
        elif l[i] == "brown":
            c6+=1
        else:
            c7+=1
    t = ceil(c0/7) * 13
    t += ceil(c1/7) * 13
    t += ceil(c2/7) * 13
    t += ceil(c3/7) * 13
    t += ceil(c4/7) * 13
    t += ceil(c5/7) * 13
    t += ceil(c6/7) * 13
    t += c7 * 16
    print(t)