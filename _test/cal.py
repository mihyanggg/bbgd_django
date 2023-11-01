print("Hello BEARU")

def sum(num1, num2) :
    return num1 + num2

def min(num1, num2) :
    return num1 - num2

def mul(num1, num2) :
    return num1 * num2

def div(num1, num2) :
    return num1 / num2

def rem(num1, num2) :
    return num1 % num2

def cal(op, num1, num2) :
    if (op == '+') :
        return( sum(num1, num2) )
    elif (op == '-') :    
        return( min(num1, num2) )
    elif (op == '*') :
        return( mul(num1, num2) )
    elif (op == '/') :
        return( div(num1, num2) )
    elif (op == '%') :
        return( rem(num1, num2) )
    else :
        print("Invalid operator entered. \n Available operators: + - * / % \n")
        return -1

def user_input() :
    op = input("operator : ")
    num1 = int(input("n1 : "))
    num2 = int(input("n2 : "))
    return op, num1, num2

def run() :
    op, n1, n2 = user_input()
    if (cal(op, n1, n2) != -1) :
        print(n1, " ", op, " ", n2, " = ", cal(op, n1, n2))
    else :
        run()

if __name__ == '__main__':
    run()

