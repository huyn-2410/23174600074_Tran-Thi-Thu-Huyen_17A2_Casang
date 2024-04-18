n=int(input("nhập số nguyên n: "))
mang=[]
for i in range(n):
    a=int(input("nhập vào phần tử:"))
    mang.append(a)
print(mang)
tong_chan=0
tong_le=0
for a in mang:
    if a%2==0:
        tong_chan += a
    else:
        tong_le += a
print(f"tổng các số chẵn của mảng nhập vào là:{tong_chan}") 
print(f"tổng các số lẻ của mảng nhập vào là:{tong_le}")       
