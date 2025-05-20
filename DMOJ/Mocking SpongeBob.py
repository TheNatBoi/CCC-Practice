ab = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
AB = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for _ in range(int(input())):
    l = list(input())
    l[0] = l[0].lower()
    case = True #next uppercase
    for i in range(1, len(l)):
        if l[i] in ab or l[i] in AB:
            if case:
                l[i] = l[i].upper()
                case = False
            else:
                l[i] = l[i].lower()
                case = True
    print("".join(l))