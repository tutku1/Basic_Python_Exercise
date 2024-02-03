def plus(a,b):
    print(a+b)
    
def minus(a,b):
    print(a-b)
    
def multiply(a,b):
    print(a*b)
    
def divide(a,b):
    print(a/b)
    
def exponentiation(a,b):
    print(a**b)
    
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = input("Which action: (plus, minus, multiply, divide, exponentiation: )")

if c == "plus":
    plus(a,b)
elif c == "minus":
    minus(a,b)
elif c == "multiply":
    multiply(a,b)
elif c == "divide":
    divide(a,b)
elif c == "exponentiation":
    exponentiation(a,b)
else :
    print("this option is not valid")
    
    

