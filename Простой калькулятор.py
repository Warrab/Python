while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "add":
        num1 = float(input('Enter a number: '))
        num2 = float(input('Enter another number: '))
        result = str(num1 + num2)
        print('The ansver is ' + result)
        # result = num1 + num2
        # print('The ansver is: ', result)
    elif user_input == "subtract":
        ...
    elif user_input == "multiply":
        ...
    elif user_input == "divide":
        ...
    else:
        print("Unknown input")
        
        
        