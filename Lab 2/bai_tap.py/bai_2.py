x=int(input("nhập 1 số nguyên: "))
chu_so_hang_nghin=x//1000
if chu_so_hang_nghin==0:
    print("số không có chữ số hàng nghìn")
elif 0< chu_so_hang_nghin<=9:
    print("chữ số hàng nghìn là: ",chu_so_hang_nghin)
else:
    phan_du=chu_so_hang_nghin % 100
    if phan_du==0:
        print(" chữ số hàng nghìn là:",0)     
    else:
        print("chữ số hàng nghìn là: ",phan_du)    
