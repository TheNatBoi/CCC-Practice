w = input().split(" ")
skills = input().split(" ")
r = []
t = []
for i in range(int(w[0])):
    r.append(input().split(" "))


for row in range(len(r)):
    for col in range(int(w[1])-1):
        if r[row][col] > skills[col]:
            pass
        # gave up