def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(num):
    return [number for number in num if prime(number)]

num = list(map(int,input().split()))
print(filter_prime(num))
    