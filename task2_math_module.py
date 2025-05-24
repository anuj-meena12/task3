import math

def calculate_math_functions(num):
    if num <= 0:
        print("Please enter a positive number for logarithm and square root calculations.")
        return

    sqrt_val = math.sqrt(num)
    log_val = math.log(num)
    sine_val = math.sin(num)

    print(f"Square root of {num} is: {sqrt_val}")
    print(f"Natural logarithm (log base e) of {num} is: {log_val}")
    print(f"Sine of {num} (radians) is: {sine_val}")

if __name__ == "__main__":
    try:
        user_input = float(input("Enter a positive number: "))
        calculate_math_functions(user_input)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
	