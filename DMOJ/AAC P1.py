imput = input()
arr = imput.split(" ")
S = int(arr[0])
R = int(arr[1])
if S**2 > 3.14*R**2:
    print("SQUARE")
else:
    print("CIRCLE")
