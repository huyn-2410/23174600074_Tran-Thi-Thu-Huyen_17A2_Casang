#hinh_1
n=int(input("nhập vào số hàng: "))
# nửa hình trên
for i in range(n ): 
    for j in range(n-i-1):
        print(' ',end="") 
    for j in range(i+1):
        print("*",end='')
    print()  
# nửa hình dưới
for i in range(n,0,-1):
    for j in range(n-i):
        print('',end="")
    for j in range(i):
        print("*",end='') 
    print()                                         