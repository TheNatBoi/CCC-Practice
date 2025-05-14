N = int(input())
count = 1
for i in range(N):
    misspell = list(input().split(" ", 1))
    M = int(misspell[0])-1
    misspelling = list(misspell[1])
    del misspelling[M]
    print(str(count) + " " + "".join(misspelling))
    count += 1