a,b,c=map(float,input("nhập các số nguyên: ").split())
max=max(a,b,c) 
min=min(a,b,c) 
so_lon_thu_hai=a+b+c-max-min
if (a>b) and (a>c) and (c>b):
    print("số lớn thứ hai là: ",so_lon_thu_hai)
elif (a>b) and (a>c) and (b>c) :
    print("số lớn thứ hai là: ",so_lon_thu_hai)
elif (b>a) and ( b>c) and (a>c):
    print("số lớn thứ hai là: ",so_lon_thu_hai)
elif (b>a) and (b>c) and (c>a):
    print("số lớn thứ hai là: ",so_lon_thu_hai)
elif (c>a) and (c>b) and (a>b):
    print("số lớn thứ hai là: ",so_lon_thu_hai)
elif (c>a) and (c>b) and (b>a):
    print("số lớn thứ hai là: ",so_lon_thu_hai)


