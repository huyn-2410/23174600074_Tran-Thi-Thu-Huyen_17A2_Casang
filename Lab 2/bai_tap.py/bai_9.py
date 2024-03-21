a,b,c=map(float,input("nhập thông số của đường thẳng là: ").split())
i1,i2,r=map(float,input("nhập tọa độ tâm và bán kính của đường tròn: ").split())
vecto_phap_tuyen=[a,b]
import math
d=math.sqrt(((a-i1)**2)+((b-i2)**2)) # khoảng cách từ tâm đến đg thẳng
if d==r:
    print("đường thẳng tiếp xúc với đường tròn")
elif d>r:
    print("đường thẳng nằm ngoài đường tròn") 
elif d<r:
    print("đường thẳng cắt đường tròn")  
else:
    print ("đường thẳng nằm trong đường tròn")         
