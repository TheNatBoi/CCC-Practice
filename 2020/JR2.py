max = int(input())
start = int(input())
per = int(input())
infected = start
day = 0

while infected <= max:
    infected += (infected * per)
    day += 1
print(day)