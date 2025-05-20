days = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
months = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
ab = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
mMax = 12
u = input()
sl = u.split("/")
m = sl[2][:2]
if sl[2][2] not in ab:
    if int(m) < 25:
        m = "20" + m
        sl[2] = m + sl[2][2:]
    elif int(m) > 25:
        m = "19" + m
        sl[2] = m + sl[2][2:]
sl = ("/".join(sl))
sp = sl.split(" ")
for i in range(len(sp)):
    if sp[i] in months.values() and int(sp[i+1][:2]) <= days[sp[i]]:
        d = sp[i+2][:2]
        if int(d) < 25:
            d = "20" + d
            sp[i+2] = d + sp[i+2][2:]
        elif int(d) > 25:
            d = "19" + d
            sp[i+2] = d + sp[i+2][2:]
print(" ".join(sp))