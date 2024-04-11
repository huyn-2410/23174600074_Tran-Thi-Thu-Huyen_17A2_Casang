n=int(input("nhập 1 số nguyên từ bàn phím: "))
ket_qua=""
if n<0:
    print("Vui lòng nhập số khác!")
else:    
    while n>0:
        if n%2==1:
           ket_qua="1"+ket_qua
        else:
           ket_qua="0"+ket_qua    
        n//=2
print("số nhị phân chuyển từ số thập phân sang là: ",ket_qua)        
