w = list(map(int, input().split()))
nums = []
words = []
for _ in range(w[0]):
    l = input().split()
    nums.append(int(l[0]))
    words.append(l[1])
out = ""
n = len(nums)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if nums[j] < nums[min_index]:
            min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
        words[i], words[min_index] = words[min_index], words[i]

for i in range(1, w[1]+1):
    for j in range(len(nums)):
        if i % nums[j] == 0:
            out += words[j]
    if out != "":
        print(out)
        out = ""
    else:
        print(i)
        # gave up