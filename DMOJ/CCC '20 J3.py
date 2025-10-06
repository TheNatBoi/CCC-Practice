h = []
w = []
for _ in range(int(input())):
    l = input().split(",")
    h.append(int(l[0]))
    w.append(int(l[1]))
print(str(min(h)-1) + "," + str(min(w)-1))
print(str(max(h)+1) + "," + str(max(w)+1))