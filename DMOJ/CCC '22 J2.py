players = int(input())
stars = 0
p = 0
for _ in range(players):
    points = int(input())
    fouls = int(input())
    cstars = 0
    cstars += 5 * points
    cstars -= 3 * fouls
    if cstars > 40:
        p += 1
    stars += cstars
if p == players:
    print(str(p) + "+")
else:
    print(str(p))