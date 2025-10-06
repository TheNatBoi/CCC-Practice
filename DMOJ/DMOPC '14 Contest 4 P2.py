wordList = []
for _ in range(int(input())):
    wordList.append(input())
centerList = []
for _ in range(int(input())):
    centerList.append("")

for word in wordList:
    minLength = 999
    center_index = 0
    for center in range(len(centerList)):
        if len(centerList[center]) < minLength:
            center_index = center
            minLength = len(centerList[center])
    centerList[center_index] += word
    print(center_index + 1)