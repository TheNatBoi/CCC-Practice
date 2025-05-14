input = input()
happy = input.count(":-)")
sad = input.count(":-(")
if happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
elif sad == 0 & happy == 0:
    print("none")
elif happy == sad:
    print("unsure")