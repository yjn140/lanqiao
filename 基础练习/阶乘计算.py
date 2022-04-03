def jinwei(num1):
    for i in range(len(num1)):
        if (num1[i] >= 10):
            num1[i + 1] += int(num1[i] / 10)
            num1[i] -= (int(num1[i] / 10) * 10)


'''
#测试函数数据
testt=[11,13,2,0]
print(testt)
jinwei(testt)
print(testt)
'''


def shuzuxiangchen(num1, num2):
    for i in range(len(num1)):
        num1[i] *= num2


'''
#测试函数数据
tesjj=[1,2,3,4]
bbb=23
shuzuxiangchen(tesjj,bbb)
print(tesjj)
'''


def printff(num1):
    flagss = False
    for i in reversed(num1):
        if i == 0 and flagss == False:
            continue
        else:
            flagss = True
            print(i, end="")


shuzu = [0 for i in range(3001)]
shuzu[0] = 1
# print(shuzu)
n = int(input())
# shuzu[0]=shuzu[0]*5
# print(shuzu)
for i in range(1, n + 1):
    shuzuxiangchen(shuzu, i)
    jinwei(shuzu)
# print(shuzu)

printff(shuzu)
