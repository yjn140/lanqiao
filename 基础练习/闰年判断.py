a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("yes")
else:
    print("no")