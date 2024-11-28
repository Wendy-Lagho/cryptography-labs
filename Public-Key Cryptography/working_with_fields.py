from sympy import mod_inverse

# Given values
g = 209
p = 991

# Compute the modular inverse
d = mod_inverse(g, p)
print(d)