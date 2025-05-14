D = int(input())
E = int(input())

for i in range(E):
    sign = input()
    donuts = int(input())
    if sign == "-":
        D -= donuts
    elif sign == "+":
        D += donuts
print(D)