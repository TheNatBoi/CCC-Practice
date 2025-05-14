num = int(input())
for i in range(num-1):
    if num % (i+1) == 0:
        print(str(num) + " is NOT Prime")
        break
    else:
        print(str(num) + " is PRIME")
        break