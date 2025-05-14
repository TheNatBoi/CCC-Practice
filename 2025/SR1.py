input = input()
arr = input.split(" ")
a = int(arr[0])
b = int(arr[1])
x = int(arr[2])
y = int(arr[3])

h = max(b,y)
w = a+x
print(2*h + 2*w)

