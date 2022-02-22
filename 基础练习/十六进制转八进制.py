n=int(input())
for i in range(n):
    if n<=10:
        s=input()
        if len(s)<=100000:
            res1=int(s,16)
            res2=oct(res1)
            print(res2[2:])