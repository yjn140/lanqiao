# 审题错了，我以为是换位打印
"""
n,m=map(int,input().split())
zimu="abcdefghijklmnopqrstuvwxyz"
k=0
for i in range(n):
    for j in range(m):
        print(zimu[int((j+k)%26)].upper(),end="")
    k+=1
    if(i<n-1):
        print("")
"""
n, m = map(int, input().split())
string = 65
for i in range(n):
    for j in range(m):
        if (string + j - i > 64 and j > i):
            print("%c" % (chr(string + j - i)), end="")
        elif (j <= i):
            print("%c" % (chr(string + i - j)), end="")
    print("")
