a1,b1,c1=map(float,input("nhập thông số của đường thẳng 1: ").split())
a2,b2,c2=map(float,input("nhập thông số của đường thẳng 2: ").split())
tich_vo_huong=(a1*a2)+(b1*b2)
if tich_vo_huong==0:
    print("Hai đường thẳng vuông góc")
else:
    if (a1==a2)  and (b1==b2) and(c1==c2):
        print("Hai đường thẳng trùng nhau") 
    elif (a1!=a2) and (b1!=b2):
        print("Hai đường thẳng cắt nhau")  
    else:
        print("Hai đường thẳng song song")      
