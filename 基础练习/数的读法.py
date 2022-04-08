"""
shu={"1":"yi","2":"er","3":"san","4":"si","5":"wu","6":"liu","7":"qi","8":"ba","9":"jiu","10":"shi","100":"bai","1000":"qian","10000":"wan","100000000":"yi"}
n=int(input())
n1=str(n)
fin=[]
zhongzhuan=0
if n>=100000000:
    if n>=1000000000 and n<2000000000:
        fin.append("10")
        fin.append("100000000")
    elif n>=2000000000:
        fin.append("2")
        fin.append("10")
        fin.append("100000000")
    else:
        fin.append(str(int(n/100000000)))
        fin.append("100000000")
if n>=10000:

该算法并非笔者想出来，转载于另一位博客大神，
链接：https://blog.csdn.net/qq_37962204/article/details/79716058
"""
n = int(input())
a = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
b = ['shi', 'bai', 'qian', 'wan', 'yi']
res = ['' for i in range(20)]
i, j = 0, 0
l = [0, 0]
while n:
    k, n = n % 10, int(n / 10)
    if k:
        if i >= 4 and l[int(i / 4) - 1] == 0:
            l[int(i / 4) - 1] = 1
            res[j], j = b[int(i / 4) + 2], j + 1
        if i % 4:
            res[j], j = b[int(i % 4) - 1], j + 1
        res[j] = a[k]
        j = j + 1
    elif j > 0 and res[j - 1] != a[0]:
        res[j], j = a[0], j + 1
    i = i + 1
if res[j - 1] != 'yi' or j <= 1 or res[j - 2] != 'shi':
    print(res[j - 1], end=' ')
for i in range(j - 2, -1, -1):
    print(res[i], end=' ')
