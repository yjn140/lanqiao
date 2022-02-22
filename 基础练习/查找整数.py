n = int(input())
s = input().split()
a = int(input())
flag2 = 1
for i in s:
    flag = False
    if int(i) == a:
        print(flag2)
        flag = True
        break
    else:
        flag2 += 1
if flag == False:
    print("-1")
