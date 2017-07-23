x=10
def factorial(num) :
    fact=1
    for x in range(1,num+1):
        fact*=x
    return fact
def addition(num1,num2) :
    num=num1+num2
    print(num)
def multiply(num1=5,num2=10):
    num=num1*num2
    print(num)
# using global variable
def example() :
    global x
    print(x)
    x+=5
    print(x)

fact=factorial(10)
print(fact)
addition(5,3)
addition(2.3,5.2)
multiply()
multiply(2)
multiply(num2=2)
multiply(3,2)
example()