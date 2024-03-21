n=int(input("nhập số ng mua vé xem phim: "))
if n==1:
    gia_ve=120.000
elif 2<= n<4:
    gia_ve=(120.000*n)-(120.000*n*0.05)
elif 4 <=n< 10:
    gia_ve=(120.000*n)-(120.000*n*0.1)
elif n>=10:
    gia_ve=(120.000*n)-(120.000*n*0.2)    
print("số tiền phải trả là: ",gia_ve)            