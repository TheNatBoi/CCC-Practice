avg = int(input())
assignments = int(input())
tot = 80 * (assignments + 1) - (avg * assignments)
if tot > 100:
    print(-1)
else:
    print(max(tot,0))