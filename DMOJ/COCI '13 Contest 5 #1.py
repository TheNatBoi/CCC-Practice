a = []
for _ in range(int(input())):
    a.append(input())
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] == "".join(list(a[j]).__reversed__()):
            print(str(len(a[i])) + " " + list(a[j])[int(len(a[j])/2)])
            continue