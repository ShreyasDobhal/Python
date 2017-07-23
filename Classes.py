class Calculator:
    def addition(num1,num2):
        add=num1+num2
        return add
    def subtraction(num1,num2):
        sub=num1-num2
        return sub
    def multiplication(num1,num2):
        mul=num1*num2
        return mul
    def division(num1,num2):
        div=num1/num2
        return div
if __name__ == '__main__' :
    print(Calculator.addition(5,3))
    print(Calculator.subtraction(5,2))
    print(Calculator.multiplication(2,7))
    print(Calculator.division(22,7))