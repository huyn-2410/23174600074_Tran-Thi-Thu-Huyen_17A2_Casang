a,b=map(float,input("nhập cân nặng và chiều cao của người đó: ").split())
BMI=a/(b**2)
if BMI<18.5:
    print("Gầy")
elif 18.5 <= BMI<=24.9:
    print("Bình thường")
elif 25 <= BMI<=29.9:
    print("Hơi béo")
else:
    print("Béo")            