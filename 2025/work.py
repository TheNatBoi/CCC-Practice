string = input()
result = []
x = string.split()
for i in x:
    if i.isdigit():
        result.append(int(x[i]))
print(result)