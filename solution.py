import sys, math

N = int(input())
TEMPS = input()
nearestPos = 5526
nearestNeg = -273
done = False

print(TEMPS, file=sys.stderr)

if N == 0:
        print(0)
        done = True
        
if N == 1:
    print(int(TEMPS))
    done = True

temps = TEMPS.split(' ')

for i in range (0,N):
    
    num = int(temps[i])
    print(num, file=sys.stderr) 
    print(done, file=sys.stderr) 
   
    if num != 0: 
        if num > 0 and num < nearestPos:
            nearestPos = num
            
        if num < 0 and num > nearestNeg:
            nearestNeg = num
    elif num == 0:
        print(0)
        done = True
 
       
if done == False:
    if -nearestNeg < nearestPos:
        print(str(nearestNeg))
    else: 
        print(str(nearestPos))
