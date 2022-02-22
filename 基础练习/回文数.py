li = []
fi = []
for i in range(1000, 10000):
    li = list(str(i))
    if ((li[0] == li[3]) & (li[1] == li[2])):
        fi.append(i)
fi.sort()
for i in fi:
    print(i)
