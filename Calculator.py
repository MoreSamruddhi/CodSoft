first_number = float(input("Enter the first number: "))

second_number = float(input("Enter the second number: "))

operation_choice = input("Enter the operation choice (+, -, *, /): ")

result = None

while True:

    if operation_choice == "+":
        result = first_number + second_number
    elif operation_choice == "-":
        result = first_number - second_number
    elif operation_choice == "*":
        result = first_number * second_number
    elif operation_choice == "/":
        result = first_number / second_number

    if result is None:
        print("Invalid operation choice.")
    else:
        print("The result is:", result)

    continue_choice = input("Continue (yes/no)? ")

    if continue_choice != "yes":
        break
    
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    
    operation_choice = input("Enter the next operation choice (+, -, *, /): ")

print("Thank You!")
