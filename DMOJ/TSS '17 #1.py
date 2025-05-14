N = int(input())
for i in range(N):
    inp = input().split(" ")
    in1 = inp[0]
    in2 = inp[1]
    in3 = inp[2]
    if in1 != in2 and in1 != in3 and in2 != in3:
        print("???")
    elif in1 != in2 and in1 != in3:
        print(in2)
    elif in2 != in3 and in2 != in1:
        print(in3)
    else:
        print(in1)