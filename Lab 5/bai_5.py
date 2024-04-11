str1=input("nhập chuỗi 1: ")
str2=input("nhập chuỗi 2: ")
str=""
min=min(len(str1),len(str2))
for i in range(min):
    str+=str1[i]+'-'+str2[i]+'-'
if len(str1)>len(str2):
    str+=str1[min:]
elif len(str1)<len(str2):
    str+=str2[min:]
if str.split("-") :
    str=str[:-2]     
print("Chuỗi đã trộn là:",str)      