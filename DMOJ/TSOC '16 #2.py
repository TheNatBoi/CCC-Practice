file = str(input())
if not file.__contains__("."):
    fileext = str(input())
    print("\"" + file + "\" - " + fileext.lower())
else:
    fileext = file.split(".")[1]
    filename = file.split(".")[0]
    print("\"" + filename + "\" - " + fileext.lower())
