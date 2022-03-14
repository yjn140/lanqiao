str1 = input()
str2 = input()

lstr1 = str1.lower()
lstr2 = str2.lower()

if (len(str1) == len(str2)):
    if (lstr1 == lstr2):
        if (str1 == str2):
            print("2")
        else:
            print("3")
    else:
        print("4")
else:
    print("1")
