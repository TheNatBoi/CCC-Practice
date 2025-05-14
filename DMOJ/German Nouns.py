for _ in range(int(input())):
    s = input().split(" ")
    c = 0
    for i in s:
        if i[0].isupper():
            c += 1
    print(c)