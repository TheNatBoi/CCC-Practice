from re import sub
for _ in range(int(input())):
    d = list(input())
    if len(d) != 26:
        print("Nope.")
    else:
        f = "".join(d)
        sub("[^a-z]", "", f)
        d = list(dict.fromkeys(list(f)))
        if len(d) != 26:
            print("Nope.")
        else:
            print("OK.")