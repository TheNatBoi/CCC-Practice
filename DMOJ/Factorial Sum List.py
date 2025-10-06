from math import factorial

nums = []
k = int(input())
while k != 0:
    nums.append(k)
    k = int(input())
for a in nums:
    arr = []
    while a not in arr:
        arr.append(a)
        b = a
        a = 0
        for i in str(b):
            a += factorial(int(i))
    print(len(arr)+1)