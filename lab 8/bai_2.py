# tính gai thừa của 1 số
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def permutations(n,r):
    if r>n:
        return 0
    else:
        return factorial(n)//factorial(n-r)    
def combinations(n,r):
        return permutations(n,r)//factorial(r)   

n=int(input("nhập phần tử n:"))     
r=int(input("nhập phần tử r:"))    
print(f"số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần là:{permutations(n,r)}")
print(f"số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần là:{combinations(n,r)}")
