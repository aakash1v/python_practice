'''
Simple interest formula is given by: Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate
Examples:

Input : P = 10000
        R = 5
        T = 5
Output :2500.0
We need to find simple interest on 
Rs. 10,000 at the rate of 5% for 5 
units of time.'''
# p = 10000
# r = 5
# t = 5
# interet = (p*r*t)/100
# print('Simple interest is ',interet)
'''
et us discuss the formula for compound interest. The formula to calculate compound interest annually is given by: 

A = P(1 + R/100) t 
Compound Interest = A -- P 
Where, '''

def compound_interest(principal,rate,time):
    # amount = principal *(pow((1+rate/100),time))
    amount = principal * (1+rate/100)**time
    ci = amount - principal
    return ci

def compound_interest(p,r,t):
    amount  = p
    for i in range(t):
        amount = amount * (1+r/100)
    
    ci = amount - p
    return ci

        

# Driver Code
print(compound_interest(10000, 10.25, 5))   