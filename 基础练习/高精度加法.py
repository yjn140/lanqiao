def anweiduqu(num1):
    num2 = []
    for i in num1:
        num2.insert(0, i)
    return num2


def jinwei(num1):
    for i in range(len(num1)):
        if (num1[i] >= 10):
            num1[i + 1] += int(num1[i] / 10)
            num1[i] -= (int(num1[i] / 10) * 10)


def shuzuxiangjia(num1, num2):
    for i in range(len(num1)):
        if i >= len(num2):
            break
        num1[i] += int(num2[i])


def printff(num1):
    flagss = False
    for i in reversed(num1):
        if i == 0 and flagss == False:
            continue
        else:
            flagss = True
            print(i, end="")


fin = [0 for i in range(120)]
a = anweiduqu(input())
b = anweiduqu(input())

shuzuxiangjia(fin, a)
jinwei(fin)
shuzuxiangjia(fin, b)
jinwei(fin)
printff(fin)
