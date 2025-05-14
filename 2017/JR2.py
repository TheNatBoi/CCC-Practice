n = int(input())
k = int(input())
K = n
for i in range(k):
    K *= 10
    n+=K
print(int(n))