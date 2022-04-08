"""
def panduankebukenenghuiwen(strs):
    lists=[]
    dirs={}
    lists=list(map(str,strs))
    for i in lists:
        if i not in dirs:
            dirs[i]=1
        else:
            dirs[i]+=1
    if len(strs)%2==0:
        for i in dirs:
            if dirs[i]%2!=0:
                return False
        return True
    else:
        su=0
        for i in dirs:
            if dirs[i]%2!=0:
                su+=1
        if su==1:
            return True
        else:
            return False

def panduanshifouhuiwen(str1):
    flags=True
    i=0
    lens=len(str1)
    while i<=(lens/2):
        if str1[i]==str1[lens-i-1]:
            i+=1
        else:
            return False
    return flags




n=int(input())
strss=input()
strs=list(strss)



changenum=0
if panduankebukenenghuiwen(strs):
     for i in range(len(strs)-1):
         if panduanshifouhuiwen(strs):
             print(changenum)
             break
         a=strs[i]
         b=strs[i+1]
         if a==b:
             continue
         if b==strs[len(strs)-i-1] and a==strs[len(strs)-i-2]:
             changenum+=1

             strs[i]=b
             strs[i+1]=a
         elif b==strs[len(strs)-i-2] or a==strs[len(strs)-i-1]:
             changenum+=1
             strs[i]=b
             strs[i+1]=a
else:
    print("Impossible")
"""