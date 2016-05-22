import sys,math;N=int(input());a=input();b=5526;c=-273;d=False;print(a,file=sys.stderr)
if N==0:print(0);d=True
if N==1:print(int(a));d=True
temps=a.split(' ')
for i in range(0,N):
    num=int(temps[i]);print(num,file=sys.stderr);print(d,file=sys.stderr)
    if num!=0: 
        if num>0 and num<b:
            b=num
        if num<0 and num>c:
            c=num
    elif num==0:
        print(0);d=True
if d==False:
    if -c<b:
        print(str(c))
    else: 
        print(str(b))
