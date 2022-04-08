import time

t=int(input())

t=int(t/1000)
t_s=time.gmtime(t)
h=str(t_s[3]) if t_s[3]>=10 else "0"+str(t_s[3])
m=str(t_s[4]) if t_s[4]>=10 else "0"+str(t_s[4])
s=str(t_s[5]) if t_s[5]>=10 else "0"+str(t_s[5])
print(h,":",m,":",s,sep="")