li = []
fi = []
for i in range(100, 1000):
    li = list(str(i))
    if (int(li[0]) * int(li[0]) * int(li[0]) + int(li[1]) * int(li[1]) * int(li[1]) + int(li[2]) * int(li[2]) * int(
            li[2])) == i:
        fi.append(i)
fi.sort()
for i in fi:
    print(i)
