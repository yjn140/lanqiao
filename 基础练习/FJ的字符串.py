n=int(input())
def FJ(n):
    if n==0:
        return ""+chr(65+n)
    else:
        return FJ(n-1)+chr(65+n)+FJ(n-1)
print(FJ(n-1))