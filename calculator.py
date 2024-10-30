from art import calc_logo,logo2    #import art to display the logo and calculator text

print (calc_logo,logo2)

def add (n1,n2):        #funtion for addition
    return n1+n2

def subtract (n1,n2):        #funtion for subtraction
    return n1-n2

def multiply (n1,n2):        #funtion for multiplication
    return n1*n2

def divide (n1,n2):        #funtion for division
    return n1/n2

operations = {        #dictionary to define each operation and its value
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculate():
    should_continue = True         #for rechecking and asking input for user to continue with previous answer
    num1 = float(input("Enter first number: "))

    while should_continue:
        for symbol in operations:            #print the operation's symbols
            print(symbol)
        operation_symbol = input("Pick an operation: " )
        num2 = float(input("Enter second number: "))
        answer = operations[operation_symbol](num1,num2)            #compute the result
        print (f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ").lower()        #ask user if they want to continue with previous answer

        if choice == 'y':
            num1 = answer
        else:
            break        
    calculate()        #if not then start the program again by asking input for number_1

calculate()
