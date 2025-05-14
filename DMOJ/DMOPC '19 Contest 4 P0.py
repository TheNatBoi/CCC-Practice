str1 = list(input())
str2 = list(input())
count = 0

for i in range(len(str1)):
    if str1[i] != str2[i]:
        count += 1

if count == 1:
    print("LARRY IS SAVED!")
else:
    print("LARRY IS DEAD!")