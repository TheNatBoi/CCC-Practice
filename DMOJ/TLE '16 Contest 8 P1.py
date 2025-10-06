t = input().split("-")[1]
arr = []
for _ in range(int(input())):
    o = input().split("-")[1]
    for i in t:
        if i not in o:
            print("no")
            break
    else: print("yes")