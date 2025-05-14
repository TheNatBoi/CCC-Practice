for _ in range(int(input())):
    g = input().split(" ")
    R = int(g[0])
    a = int(g[1])
    b = int(g[2])
    c = 0
    for i in range(R+1):
        if i % a == 0 or i % b == 0:
            c+=1

    print(c-1)