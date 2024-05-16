def sumPdivisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    
    return total

n = 36
print(f"Tổng các ước số chính của {n} là: {sumPdivisors(n)}")