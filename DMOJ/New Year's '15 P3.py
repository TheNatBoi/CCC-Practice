n = 2 * int(input()) - 1
a = int((n+1)/2 - 1)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
l = []
for _ in range(n):
    l.append([])
for i in l:
    for _ in range(n):
        i.append("")
h = 0
for _ in range(a+1):
    for row in range(len(l)):
        for col in range(len(l[row])):
            if row == h or col == h or col == len(l[row])-(1+h) or row == len(l)-(1+h):
                if l[row][col] == "":
                    l[row][col] = alphabet[a]
    h+=1
    a-=1

for r in l:
    g = "".join(r)
    print(g)