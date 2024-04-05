numbers=[]
sum=0
while sum<=1000:
    n=int(input("nhập 1 số nguyên: "))
    if n>0:
        numbers.append(n)
        sum+=n
    else:
        print("vui lòng nhập lại!")
#a.         
so_le=[n for n in numbers if n%2!=0]
print("các số lẻ là:",so_le)
#b.                 
so_chan=[n for n in numbers if n%2==0] 
print("các số chẵn là:",so_chan)
#c.
so_luong=len(numbers) 
print("số lượng số nguyên đã nhập là:",so_luong)               
