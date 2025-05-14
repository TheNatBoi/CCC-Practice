n = int(input())
y = list(input())
t = list(input())
count = 0

for i in range(n):
    if "c" in y[i] and "c" in t[i]:
        count += 1
print(count)