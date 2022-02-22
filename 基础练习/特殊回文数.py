n = int(input())

for i in range(10000, 999999):
    li = []
    li = list(str(i))
    if i <= 99999:
        if (li[0] == li[4]) & (li[1] == li[3]):
            if (int(li[0]) + int(li[1]) + int(li[2]) + int(li[3]) + int(li[4])) == n:
                print(i)
    elif i >= 100000:
        if (li[0] == li[5]) & (li[1] == li[4]) & (li[2] == li[3]):
            if (int(li[0]) + int(li[1]) + int(li[2]) + int(li[3]) + int(li[4]) + int(li[5])) == n:
                print(i)
