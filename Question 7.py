#check if a number is prime
def prime_check(n, p):
    p = 2
    if n<=1: #checks if number is less than 1
        return
    elif p>=n: #checks if 2 is greater than n
        print(n) 
    elif n % p !=0: #checks if n remainder 2 is not equal to 0 which means prime
        prime_check(n, p + 1)
