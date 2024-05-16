# kiểm tra số nguyên tố
def so_nguyen_to(n):
    if n<=1:
        return False
    if n==2:
        return True    
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1):
        if n%i==0:
            return False
        return True
def print_twin_primes(limit):
    for n in range(3,limit,2):
        if so_nguyen_to(n) and so_nguyen_to(n+2):
            print(f"{n},{n+2}")

print_twin_primes(1000)        

    

