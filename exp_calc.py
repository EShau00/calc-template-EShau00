import re

def eval(string):
    '''
    MDAS:   Multiplication and Division
            Addition and Subtraction
    '''

    def perform_operation(parsed, operation):
        operation_index = parsed.index(operation)
        parsed.pop(operation_index)
        a = float(parsed.pop(operation_index-1))
        b = float(parsed.pop(operation_index-1))
        if operation == '^':
            parsed.insert(operation_index-1, str(a ** b))
        elif operation == '*':
            parsed.insert(operation_index-1, str(a * b))
        elif operation == '/':
            parsed.insert(operation_index-1, str(a / b))
        elif operation == '+':
            parsed.insert(operation_index-1, str(a + b))
        elif operation == '-':
            parsed.insert(operation_index-1, str(a - b))

    parsed = re.split("([\(\)\^\*/\+-])", string)
    parsed = [entry.strip() for entry in parsed]
    parsed = list(filter(lambda x : x != '', parsed))

    while len(parsed) != 1:

        # Performs parentheses stufes
        while '(' in parsed and ')' in parsed:
            op_index = parsed.index('(')
            temp = ""
            # We don't want the '(' thing
            parsed.pop(op_index)
            while parsed[op_index] != ')':
                temp += parsed.pop(op_index)
            # We don't want the '(' thing
            parsed.pop(op_index)
            # We eval it and pop it back in
            parsed.insert(op_index, eval(temp))

        # Performs exponential operations
        while '^' in parsed:
            perform_operation(parsed, '^')

        # Performs multiplication and division operations
        while '*' in parsed or '/' in parsed:

            # We can guarentee division exists
            if '*' not in parsed:
                perform_operation(parsed, '/')
            
            # We can guarentee multiplication exists
            elif '/' not in parsed:
                perform_operation(parsed, '*')
            
            # We can guarentee both exist

            # Left to Right
            elif parsed.index('*') < parsed.index('/'):
                perform_operation(parsed, '*')
            
            # Left to Right
            elif parsed.index('/') < parsed.index('*'):
                 perform_operation(parsed, '/')
            
            # We don't need an else statement because these 5 statements cover all cases

        # Performs addition and subtraction operations
        while '+' in parsed or '-' in parsed:

            # We can guarentee division exists
            if '+' not in parsed:
                perform_operation(parsed, '-')
            
            # We can guarentee multiplication exists
            elif '-' not in parsed:
                perform_operation(parsed, '+')
            
            # We can guarentee both exist

            # Left to Right
            elif parsed.index('+') < parsed.index('-'):
                perform_operation(parsed, '+')
            
            # Left to Right
            elif parsed.index('-') < parsed.index('+'):
                 perform_operation(parsed, '-')
            
            # We don't need an else statement because these 5 statements cover all cases

    return(float(parsed.pop()))

def run():
    
    print("Welcome to Eric and Alejandro's 4-function calculator!")
    print("We have full faith in you to make correct expressions.")
    print("Otherwise Python is gonna spit stuff out at you lol")
    print("Enter \"quit\" to quit at any time.\n")
    string = input("Input: ")

    while string != "quit":
        print(f"Output: {eval(string)}\n")
        string = input("Input: ")

    print("\nWe hope you enjoyed your stay!")


run()