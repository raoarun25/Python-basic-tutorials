
# Fibonacci series

def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)


 # check whether its prime number or not

def prime(num):
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            break
    else:
        print num, "is prime number"


# factorial of a number 

def factorial(num):
    x = 1
    for i in range(2,num+1):
        x = x * i
    print x
            

# function to check string is  
# palindrome or not  
def isPalindrome(str): 
    # Run loop from 0 to len/2  
    for i in xrange(0, len(str)/2): 
        print i, len(str)/2 
        if str[i] != str[len(str)-i-1]: 
            return False
    return True




    


