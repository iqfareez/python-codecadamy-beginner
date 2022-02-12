def calculate(num1 : int, operator: str, num2 : int ) -> int:
    # if there is a bwtter way kindly let me know
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "/":
            return num1 / num2
        case "*":
            return num1 * num2

first_number = 3 # change first number
second_number = 4 # change second number
answer = calculate(first_number, "*", second_number) # change operator
print(answer)
