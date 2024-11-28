from sympy import factorint, isprime, primitive_root

# Given prime modulus
p = 28151

# Find the smallest primitive root (generator) of F_p
g = primitive_root(p)
print(g)