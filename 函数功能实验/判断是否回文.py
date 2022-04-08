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

str11="accda"
print(panduanshifouhuiwen(str11))
