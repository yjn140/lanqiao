n = int(input())
list = []
for i in range(0, n):
    l, r = map(int, input().split())
    list.append([l, r])
list.sort(key=lambda x: x[1])
s = []
while len(list) != 0:
    minr = list[0][1]
    s.append(minr)
    k = 0
    l = list[k][0]
    while minr >= l:
        k += 1
        if k < len(list):
            l = list[k][0]
        else:
            minr = -1
    del list[0:k]
print(len(s))
