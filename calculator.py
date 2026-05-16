val1 = float(input("Enter the first value: "))
val2 = float(input("Enter the second value: "))
print("- + * /")
method = input("Enter the type of calculation you want: ")
answer = 0
if method == "-":
    answer = val1 - val2
elif method == "+":
    answer = val1 + val2
elif method == "*":
    answer = val1 * val2
elif method == "/":
    if val2 == 0:
        print("Division by zero")
        answer = "Undefined0"
    else:
        answer = val1 / val2
else:
    print("Invalid type of calculation")
print(f"Answer to {val1} {method} {val2} = {answer}")