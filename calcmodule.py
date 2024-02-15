import time
import initmodule
import sys
import random

commands = ['s', 'c', 'exit']
operators = ['+', '-', '*', '/']
user_input = ''
sliced_string = []
processed_array = []  
previous_result = 0
next_state = ''
exit_msg = ["Thanks for using TermCalc :) Hope to see you again soon !", 
            "Sad to see you go... Hope you enjoyed your time using TermCalc! =)",
            "Farewell! Don't forget to check out the repository @cetincetindag/term-calc ",
            "Goodbye! Come back soon? Thank you for using TermCalc! :3",
            "Bye-bye! Everything will be smoother when you come back :3."]


def memclear():
    global user_input   
    global sliced_string    
    global processed_array
    global previous_result    
    global next_state

    user_input = '' 
    next_state = ''
    sliced_string.clear()
    processed_array.clear()
    previous_result = 0
    print("Memory cleared !!")
    print("=============")


def get_state():
    global next_state

    next_state = input("input: ")

def store_result(var):
    global previous_result

    if var.isidentifier():
        var_name = var
        var = previous_result 
        print(f"Result stored in variable '{var_name}'.")
        initmodule.init_sequence()

    else:
        print("Invalid variable name. Please use a valid identifier.")
        get_state()

def get_input():
    global user_input
    global sliced_string 

    user_input = input("Please enter your input below:\n")
    if user_input != 'exit':
        sliced_string = [ch for ch in user_input]
    elif user_input == 'exit':
        exit_func()


def seperate_nums():
    global sliced_string
    global processed_array

    current_num = ''
    for char in sliced_string:
        if char.isdigit():
            current_num += char
        elif char in operators:
            if current_num:
                processed_array.append(current_num)
                current_num = ''
            processed_array.append(char)
    if current_num:
        processed_array.append(current_num)

    sliced_string = []     

def perform_calc():
    global processed_array
    global previous_result
    global next_state

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def apply_calculation(operator, operand):
        operator = operators.pop()
        right_operand = float(operands.pop())
        left_operand = float(operands.pop())

        if operator == '+':
            operands.append(left_operand + right_operand)
        elif operator == '-':
            operands.append(left_operand - right_operand)
        elif operator == '*':
            operands.append(left_operand * right_operand)
        elif operator == '/':
            if right_operand == 0:
                raise ValueError("Division by zero not possible.")
            operands.append(left_operand / right_operand)

    operators = []
    operands = []

    for token in processed_array:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            operands.append(token)
        elif token in precedence:
            while operators and precedence[operators[-1]] >= precedence[token]:
                apply_calculation(operators, operands)
            operators.append(token)

    while operators:
        apply_calculation(operators, operands)
        previous_result = operands[0]

    print(f"Result: {previous_result}")
    time.sleep(0.1)   
    print("-Type s to store the result in a variable to use in your next calculation.")
    print("-Type c to clear everything and start a new calculation.")
    get_state()

def exit_func():
    time.sleep(0.2)
    print(u"\u001b[32m +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")
    sys.exit(exit_msg[random.randint(0,(len(exit_msg)-1))])

def select_state():
    global commands
    global next_state

    if next_state in commands:
        if next_state == 'c':
            memclear()
            initmodule.init_sequence()
        elif next_state == 's':
            var = input("Type your variable name to store the result\n(only alphanumeric characters and underscores allowed)\ninput: ")
            if var in ['x', 'y', 'z ']:
                store_result(var)
            else:
                print("Invalid input, please try again.")
                get_state()
        elif next_state == 'exit':
                exit_func()








