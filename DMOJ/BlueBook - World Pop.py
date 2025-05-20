p = (float(input()))
y = int(input())
n = int(input())
f = int(input())

for i in range(f-y):
    n *= ((100 + p)/100)
print(round(n))