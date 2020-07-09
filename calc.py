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
        if operation == '*':
            parsed.insert(operation_index-1, str(a * b))
        elif operation == '/':
            parsed.insert(operation_index-1, str(a / b))
        elif operation == '+':
            parsed.insert(operation_index-1, str(a + b))
        elif operation == '-':
            parsed.insert(operation_index-1, str(a - b))

    parsed = re.split("([\*/\+-])", string)
    parsed = [entry.strip() for entry in parsed]

    while len(parsed) != 1:

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
    print("Enter \"quit\" to quit at any time.\n")
    string = input("Input: ")

    while string != "quit":
        print(f"Output: {eval(string)}\n")
        string = input("Input: ")

    print("Welcome to Eric and Alejandro's 4-function calculator!")
    print("We hope you enjoyed your stay!")


run()