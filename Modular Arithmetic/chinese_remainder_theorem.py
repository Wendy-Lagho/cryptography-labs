def invmod(x, y):
    """Calculate the modular inverse of x modulo y using the Extended Euclidean algorithm."""
    x0, x1, y0, y1 = 1, 0, 0, 1
    while y != 0:
        q = x // y
        x, y = y, x % y
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0

def ChineseRemainderGauss(n, N, a):
    """Solves for x using the Chinese Remainder Theorem."""
    x = 0
    for i in range(len(n)):
        ai = a[i]
        ni = N // n[i]
        # Modular inverse of ni modulo n[i]
        inverse_ni = invmod(ni, n[i])
        x += ai * ni * inverse_ni
    return x % N

# Given moduli and remainders
n = [5, 11, 17]
a = [2, 3, 5]
N = 5 * 11 * 17  # Calculate the product of all moduli

# Calculate the solution for x
x_solution = ChineseRemainderGauss(n, N, a)
print(x_solution)
