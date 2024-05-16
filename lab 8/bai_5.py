def sumPdivisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    
    return total
def is_amicable(n1,n2):
    return sumPdivisors(n1)==n2 and sumPdivisors(n2)==n1

n1=220
n2=284
if is_amicable(n1, n2):
    print(f"{n1} và {n2} là cặp số amicable.")
else:
    print(f"{n1} và {n2} không phải là cặp số amicable.")
