
# simple calculator 


def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("enter choice(1/2/3/4) : ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print num1,"+",num2,"=", add(num1,num2)

if choice == 2:
    print num1,"-",num2,"=", substract(num1,num2)

if choice == 3:
    print num1,"*",num2,"=", multiply(num1,num2)

if choice == 4:
    print num1,"/",num2,"=", divide(num1,num2)
