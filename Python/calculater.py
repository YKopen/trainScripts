import math

def calculater(num1, method, *num2):
    if method == '+':
        return num1 + num2
    if method == '-':
        return num1 - num2
    if method == '*':
        return num1 * num2
    if method == '/':
        return num1 / num2
    if method == '**':
        return num1 ** num2
    if method == 'r':
        return math.sqrt(num1)

if __name__ == "__main__":
    num1 = int(input("First number is ?:"))
    flag = True
    while(flag):
        method = input("Method is ? (ex: +, -, *, **, /, r):")
        if method == 'r':
            calculate = calculater(num1, method)
        else:
            num2 = int(input("Second number is ?:"))
            calculate = calculater(num1, method, num2)
        if input('Continue ? (y/n):') == 'y':
            num1 = calculate
        else:
            flag = False
    print('Answer is {} !'.format(calculate))
