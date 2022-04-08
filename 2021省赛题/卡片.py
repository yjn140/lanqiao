A=[2021 for i in range(10)]
for i in range(1,20210):
    t=list(str(i))
    for j in t:
        A[int(j)]-=1
    if -1 in A or -2 in A or -3 in A:
        print(i-1)
        break