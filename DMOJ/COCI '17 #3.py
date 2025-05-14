N = int(input())
passwords = []
count = 0
for i in range(N):
    passwords.append(input())
for password in passwords:
    for _ in range(len(passwords)):
        if password.__contains__(passwords[_]):
            count += 1
print(count - passwords.__len__())