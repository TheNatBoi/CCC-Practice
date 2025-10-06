contacts = {}
for _ in range(int(input())):
    l = input().split()
    contacts.update({int(l[1]):l[0]})
calls = {}
for _ in range(int(input())):
    d = int(input())
    t = calls.get(contacts[d], 0)
    calls.update({contacts[d]:t+1})
m = -1
names = list(contacts.values())
numbers = list(contacts.keys())
for i in calls:
    if calls[i] > m:
        m = calls[i]
        c = i
    elif calls[i] == m:
        if numbers[names.index(i)] < numbers[names.index(c)]:
            c = i

print(c)