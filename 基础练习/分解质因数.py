def zhishu(num1):
    for i in range(2, num1):
        if num1 % i == 0:
            return False
    return True


def zhiyinshufenjie(num1):
    fin = []
    while (not zhishu(num1)):
        for j in range(2, num1 + 1):
            if (num1 % j == 0):
                fin.append(j)
                num1 = int(num1 / j)
                break
    if (num1 != 1):
        fin.append(num1)
    return fin


def printt(num1, num2):
    for i in range(num1, num2 + 1):
        print("%d=" % i, end="")
        flags = len(zhiyinshufenjie(i))
        for j in zhiyinshufenjie(i):
            print(j, end="")
            if flags > 1:
                print("*", end="")
                flags -= 1
        print("", end="\n")


a, b = map(int, input().split())
printt(a, b)
