vowels = ['a', 'e', 'i', 'o', 'u', 'y']
l = list(input())
t = 0
for i in l:
    if i in vowels:
        t += 1
if t > 1:
    print("good")
else:
    print("bad")