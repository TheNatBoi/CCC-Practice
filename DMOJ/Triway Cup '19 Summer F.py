from math import sqrt
start = list(map(int, input().split(" ")))
end = list(map(int, input().split(" ")))
print(max(abs(start[0] - end[0]), abs(start[1] - end[1]), abs(start[2] - end[2])))
print(int(sqrt(((int(start[0]) - int(end[0])) ** 2) + ((int(start[1]) - int(end[1])) ** 2) + ((int(start[2]) - int(end[2])) ** 2))))
print(abs(int(start[0]) - int(end[0])) + abs(int(start[1]) - int(end[1])) + abs(int(start[2]) - int(end[2])))