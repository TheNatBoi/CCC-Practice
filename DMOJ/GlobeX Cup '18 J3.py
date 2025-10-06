from math import sqrt

def sum_of_digits(h):
    tot = 0
    for i in range(len(str(h))):
        tot += int((list(str(h))[i]))
    return tot

def is_prime(k):
    if k < 2:
        return False
    for i in range(2, int(sqrt(k)) + 1):
        if k%i==0:
            return False
    return True

t = 0
for _ in range(int(input())):
    num = int(input())
    if is_prime(num) and is_prime(sum_of_digits(num)):
        t+=1
print(t)