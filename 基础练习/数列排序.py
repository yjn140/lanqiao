a = input()
s = input().split()
ss = sorted(list(map(int, s)))
for i in ss:
    print("%d " % int(i), end="")
