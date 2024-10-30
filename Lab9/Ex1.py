with open("Names.txt",mode="r") as textFile:
    NameList = textFile.read()
    print(type(textFile))
    print(NameList)

separatedList = NameList.split("\n")
print(separatedList)
count = len(separatedList)
print(f"There are {count} names in the file")