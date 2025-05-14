n = int(input())
magnets = list(input())
right = 0
wrong = 0

for i in range(0, len(magnets), 2):
    if magnets[i] == 'I' and magnets[i+1] == 'U':
        right += 1
    else:
        wrong += 1
print(right, wrong)