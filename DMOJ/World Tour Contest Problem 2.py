s = input()
if s[len(s)-1] == "1" and s[len(s)-2] != "1":
    print(s + " кочерга")
elif s[len(s)-1] == "2" or s[len(s)-1] == "3" or s[len(s)-1] == "4" and s[len(s)-2] != "1":
    print(s + " кочерги")
else:
    print("3 кочерги" + " и " + str(s-3) + "дополнительных")