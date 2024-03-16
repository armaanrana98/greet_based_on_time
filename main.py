try:
    again = True
    while again:
        again = False
        a = int(input("Enter first number: "))
        print("Choose operator: +, -, *, /")
        type_operator = input("Enter operator: ")
        b = int(input("Enter second number: "))

        if type_operator == "+":
            print(a + b)
        elif type_operator == "-":
            print(a - b)
        elif type_operator == "*":
            print(a * b)
        elif type_operator == "/":
            if b != 0:
                print(a / b)
            else:
                print("Denominator is zero")
        else:
            print("Choose Correct Operator")
        print("Want to try again? Type 'True' else 'False'")
        again = input().lower() == 'true'
except ValueError as e:
    print("Error:", e)
