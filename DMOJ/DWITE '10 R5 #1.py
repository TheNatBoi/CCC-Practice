for i in range(5):
    text = list(input().split(" "))
    logo = list(text[0])
    outLogo = logo
    colors = list(text[1])
    color = input()
    if color.__contains__("+"):
        splitColors = list(color.split("+"))
        for j in range(len(splitColors)):
            currentColor = splitColors[j]
            for k in range(len(colors)):
                if colors[k] == currentColor:
                    outLogo[k] = "_"
        print("".join(outLogo))
    else:
        for k in range(len(colors)):
            if colors[k] == color:
                outLogo[k] = "_"
        print("".join(outLogo))