num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
       'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one',
       'twenty two', 'twenty three']
fi = input().split()
h = int(fi[0])
m = int(fi[1])
if m == 0:
    print(num[h] + " o'clock")
else:
    if m <= 20:
        print(num[h] + " " + num[m])
    else:
        if m == 30:
            print(num[h] + " thirty")
        elif m == 40:
            print(num[h] + " forty")
        elif m == 50:
            print(num[h] + " fifty")
        k = int(m / 10) * 10
        if k == 30:
            print(num[h] + " thirty" + " " + num[m - k])
        elif k == 40:
            print(num[h] + " forty" + " " + num[m - k])
        elif k == 50:
            print(num[h] + " fifty" + " " + num[m - k])
        else:
            print(num[h] + " " + num[k] + " " + num[m - k])
