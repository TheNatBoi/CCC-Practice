closestToA = ['b','c']
closestToE = ['d','f','g']
closestToI = ['h','k','k','l']
closestToO = ['m','n','p','q']
closestToU = ['r','v','w','x','y','z']
consonants = ['b','c','d','f','g','h','k','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']
word = list(input())
output:str = ''

for i in range(len(word)):
    if word[i] in consonants:
        output += word[i]
        if word[i] in closestToA:
            output += "a"
        elif word[i] in closestToE:
            output += "e"
        elif word[i] in closestToI:
            output += "i"
        elif word[i] in closestToO:
            output += "o"
        else:
            output += "u"
        for j in range(len(consonants)):
            if (consonants[j] == word[i]) & (word[i] != "z"):
                output += consonants[j+1]
            elif (consonants[j] == word[i]) & (word[i] == "z"):
                output += "z"
    else:
        output += word[i]
print(output)
