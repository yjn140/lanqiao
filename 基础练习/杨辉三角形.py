n = int(input())
list1 = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if j == 0:
            list1[i][j] = 1
        else:
            list1[i][j] = list1[i - 1][j - 1] + list1[i - 1][j]
for i in range(n):
    for j in range(n):
        if list1[i][j] != 0:
            print(list1[i][j], end=" ")
    print("")
