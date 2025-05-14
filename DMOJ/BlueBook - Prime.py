from math import sqrt, floor

T = int(input())
for i in range(T):
    N = int(input())
    if N == 1:
        print(0)
        continue
    is_prime = True
    for j in range(2, floor(sqrt(N)) + 1):
        if N % j == 0:
            is_prime = False
            break
    if is_prime:
        print(1)
    else:
        print(0)