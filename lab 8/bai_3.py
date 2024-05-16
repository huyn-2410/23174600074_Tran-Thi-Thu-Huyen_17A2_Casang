#1
def cubesum(n):
    if n==0:
        return 0
    else:
        return (n%10)**3+ cubesum(n//10)
n=int(input("nhập n: "))    
print (f"tổng các số lập phương của các chữ số riêng lẻ của {n} = {cubesum(n)}")
#2
print("các số trong giới hạn là:")
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    sum_a= sum(d**3 for d in digits)
    return sum_a == n
def print_armstrong(limit):
    for num in range(1,limit):
        if is_armstrong(num):
            print(num)
limit=1000
print_armstrong(limit)
