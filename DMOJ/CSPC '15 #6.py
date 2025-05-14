avg = 0
names = []
div = []
eRoboticsTime = 0
e = 0
dRoboticsTime = 0
d = 0
pRoboticsTime = 0
p = 0
bRoboticsTime = 0
b = 0
sRoboticsTime = 0
s = 0
hours = []
for _ in range(int(input())):
    q = input().split(" ")
    names.append(q[0])
    div.append(q[1])
    if q[1] == "Business":
        bRoboticsTime += float(q[4]) * int(q[5])
        b+=1
    elif q[1] == 'Electrical':
        eRoboticsTime += float(q[4])
        e+=1
    elif q[1] == 'Design':
        dRoboticsTime += float(q[4])
        d+=1
    elif q[1] == 'Programming':
        pRoboticsTime += float(q[4])
        p+=1
    elif q[1] == 'Strategy':
        sRoboticsTime += float(q[4])
        s+=1
averages = [eRoboticsTime/e, dRoboticsTime/d, pRoboticsTime/p, bRoboticsTime/b, sRoboticsTime/s]
for i in range(len(names)):
    pass