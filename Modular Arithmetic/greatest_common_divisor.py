def gcd(a, b):
    """Calculates the Greatest Common Divisor (GCD) of two numbers using Euclid's algorithm."""
    while b != 0:
        a, b = b, a % b
    return a

# Test case:
a = 66528
b = 52920
result = gcd(a, b)

# Print the result so it shows up in the console
print(f"The GCD of {a} and {b} is: {result}")
