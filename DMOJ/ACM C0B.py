T = int(input())
for i in range(T):
    N = int(input())
    pile1 = list(input())
    pile2 = list(input())
    outPile = []
    for j in range(len(pile1)):
        outPile.append(pile1[j])
        outPile.append(pile2[j])
    outPile.reverse()
    print(''.join(outPile))
