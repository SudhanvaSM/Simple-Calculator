from art import calc_logo,logo2

print (calc_logo,logo2)

def add (n1,n2):
    return n1+n2

def subtract (n1,n2):
    return n1-n2

def multiply (n1,n2):
    return n1*n2

def divide (n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculate():
    should_continue = True
    num1 = float(input("Enter first number: "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: " )
        num2 = float(input("Enter second number: "))
        answer = operations[operation_symbol](num1,num2)
        print (f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ").lower()

        if choice == 'y':
            num1 = answer
        else:
            break
    calculate()

calculate()