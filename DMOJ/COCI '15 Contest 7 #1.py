arr = input()
if arr == "{}":
    print("{\n}")
else:
    d = arr.split("{")
    e = d[1].split("}")
    f = e[0].split(",")
    print("{")
    for i in range(len(f)):
        if i == len(f)-1:
            print("  " + f[i])
        else:
            print("  " + f[i] + ",")
    print("}")