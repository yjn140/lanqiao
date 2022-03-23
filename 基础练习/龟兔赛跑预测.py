v1, v2, t, s, l = map(int, input().split())
times = 0
tu = 0
gui = 0
while not (tu >= l or gui >= l):
    if (tu - gui >= t):
        times += s
        if (gui + v2 * s > l):
            gui += v2 * s
            times = times - ((gui - l) / v2)
            gui = l
        else:
            gui += v2 * s
    else:
        tu += v1
        gui += v2
        times += 1

if (gui > tu):
    print("T")
elif (tu > gui):
    print("R")
else:
    print("D")
print(int(times))
