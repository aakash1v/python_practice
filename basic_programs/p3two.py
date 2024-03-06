'''
Prime Factorization Method to find Factorial
Initialize the factorial variable to 1.
For each number i from 2 to n, do the following:
a. Find the prime factorization of i.
b. For each prime factor p and its corresponding power k in the factorization of i, multiply the factorial variable by p raised to the power of k.
Return the factorial variable.
'''
# Python 3 program to find factorial
# of a given number using prime
# factorization method.
 
# Function to find prime factors of a number
def primeFactors(n):
    factors = {}
    i = 2
    while i*i <= n:
        
        while n % i == 0: #main condition... 
            if i not in factors:
                factors[i] = 0
                
            factors[i] += 1
            n =n // i
        i += 1

    if n > 1:
        if n not in factors:
            factors[n] = 0
        factors[n] += 1

    return factors 
 
# Function to find factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n+1):
        factors = primeFactors(i)
        for p in factors:
            result *= p ** factors[p]
    return result
 
# Driver Code
num = 12
print("Factorial of", num, "is", factorial(num))
# print(primeFactors(num))
