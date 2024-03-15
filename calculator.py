"""
Simple calculator

Input first number
input function
Input second number
---------
code made in September 2023
"""

try:
    calc_num_one = int(input("1st Number: "))
    function = input("Function (+, -, *, /): ")
    calc_num_two = int(input("2st Number: "))
    print (" ")
except ValueError:
    print("Operation cancel doe to invalid input.")
else:
    func_oes = ["+", "-", "*", "/"]
    if function  not in func_oes:
        print("Invalid function.")
    else:
        if function  == "+":
            resultado = calc_num_one + calc_num_two
            print("The sum is:", resultado)
        elif function  == "-":
            resultado = calc_num_one - calc_num_two
            print("The subtraction is:", resultado)
        elif function  == "*":
            resultado = calc_num_one * calc_num_two
            print("The product is:", resultado)
        elif function  == "/":
            if calc_num_two != 0:
                resultado = calc_num_one / calc_num_two
                print("The quotient is:", resultado)
            else:
                print("Cannot divide by zero.")
