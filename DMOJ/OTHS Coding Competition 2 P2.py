m = int(input())
i = []
for _ in range(int(input())):
    i.append(int(input()))
if m > max(i):
    print("run away")
else:
    print("fight")