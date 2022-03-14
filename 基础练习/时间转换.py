times = int(input())

if times < 60:
    print("0:0:%d" % times)
elif ((times < 3600) & (times >= 60)):
    print("0:%d:%d" % (int(times / 60), int(times - (60 * int(times / 60)))))
else:
    print("%d:%d:%d" % (int(times / 3600), int((times - 3600 * (int(times / 3600))) / 60),
                        int(times - 3600 * (int(times / 3600)) - 60 * (
                            int((times - 3600 * (int(times / 3600))) / 60)))))
