"""list1=[1,2,3,7,8,9,44,66,7]
var1 = sorted(list1)
list1.remove(1)
print(list1)"""

n = int(input())
varlist = list(map(int, input().split()))
summ = 0
while (len(varlist) >= 2):
    varlist = sorted(varlist)
    a = varlist[0]
    b = varlist[1]
    summ += (a + b)
    del (varlist[0])
    del (varlist[0])
    varlist.append(a + b)
print(summ)
