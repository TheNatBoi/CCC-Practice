for _ in range(int(input())):
    l = list(map(int, input().split()))
    if l[0] * l[1] == l[2]:
        print("POSSIBLE DOUBLE SIGMA")
    else:
        print("16 BIT S/W ONLY")