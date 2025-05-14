N = int(input())
non = ["Cl", "Br", "Xe", "Kr", "Si", "As", "Rn", "Ne", "He", "H", "C", "N", "O", "F", "P", "S", "I", ]
h = 0

for i in range(N):
    comp = input().split(" ")
    for j in range(len(comp)):
        if comp[j] not in non:
            print("Not molecular!")
            h = 0
            break
        elif comp[j] in non:
            h += 1
    if h == len(comp):
        print("Molecular!")
        h = 0