#a.
S1=0
for i in range(2000,4001):
    if i%7==0 and i%5!=0:
        S1+=i
print("Tổng là:",S1)
#b.
S2=0
for i in range(500,1001):
    if i%4==0 and i%6!=0:
        S2+=i
print("Tổng là:",S2)        
