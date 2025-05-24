def factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact

if __name__ == "__main__":
    sample_number = 5
    result = factorial(sample_number)
    if result is not None:
        print(f"Factorial of {sample_number} is: {result}")
    else:
        print("Factorial is not defined for negative numbers.")
