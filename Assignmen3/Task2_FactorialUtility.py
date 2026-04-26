# Task 2 - Recursive Function: Factorial Utility
def factorial(n):
    """
        Calculates the factorial of n using recursion.
        Includes handling for edge cases and negative inputs.
    """
    # Handle negative numbers (Error Case)
    if n < 0:
        print('Error: Factorial is not defined for negative numbers')
        return None
    # Factorial of 0 or 1 is always 1
    elif n == 0 or n == 1:
        return 1

    #  Recursive step: n! = n * (n-1)!
    return n * factorial(n - 1)


# --- Testing the function ---
# Test Case 1: Positive number
print(f"factorial(5): {factorial(5)}")

# Test Case 2: Edge case zero
print(f"factorial(0): {factorial(0)}")

# Test Case 3: Negative number
print(f"factorial(-3): {factorial(-3)}")
