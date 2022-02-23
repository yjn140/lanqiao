num = int(input())
flag = 0


def find(n):
    global flag
    if flag == n:
        return flag
    li = list(map(int, list(str(n))))
    li.sort()
    if li[0] == 0:
        if li[1] == 0:
            if li[2] == 0:
                if li[3] == 0:
                    print(n)
                else:
                    flag = n
                    return find((int(str(li[3]))) * 1000 - (int(str(li[3]))))
            else:
                flag = n
                return find((int(str(li[3]) + str(li[2]))) * 100 - (int(str(li[2]) + str(li[3]))))
        else:
            flag = n
            return find(
                (int(str(li[3]) + str(li[2]) + str(li[1]))) * 10 - (int(str(li[1]) + str(li[2]) + str(li[3]))))
    else:
        flag = n
        return find((int(str(li[3]) + str(li[2]) + str(li[1]) + str(li[0]))) - (
            int(str(li[0]) + str(li[1]) + str(li[2]) + str(li[3]))))


print(find(num))
