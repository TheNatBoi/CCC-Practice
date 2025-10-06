from math import sqrt


def digital_sum_even(n):
    return True if sum(int(i) for i in str(n)) % 2 == 0 else False
def increasing_digits(n):
    s = str(n)
    for dig in range(len(s)-1):
        if s[dig] >= s[dig+1]:
            return False
    return True
def divisible_by_perfect_square(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i**2 == 0:
            return True
    return False

for _ in range(5):
    t = 0
    l = input().split()
    for j in range(int(l[0]), int(l[1])+1):
        if increasing_digits(j):
            if digital_sum_even(j) and not divisible_by_perfect_square(j): t+=1
    print(t)