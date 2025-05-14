input1 = int(input())
input2 = int(input())
input3 = int(input())
input4 = int(input())

if input1 == 8 or input1 == 9:
    if input2 == input3:
        if input4 == 8 or input4 == 9:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")