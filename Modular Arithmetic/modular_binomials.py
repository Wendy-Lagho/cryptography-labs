from sympy import symbols, Eq, mod_inverse, solve

# Define inputs
N = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161
c1 = 1234567890  # Replace with the actual value of c1
c2 = 9876543210  # Replace with the actual value of c2
e1 = 3  # Replace with the actual value of e1
e2 = 5  # Replace with the actual value of e2

# Define symbols
p, q = symbols('p q')

# Step 1: Invert c1 and c2 using the modular inverse
C1 = pow(c1, mod_inverse(e1, N), N)
C2 = pow(c2, mod_inverse(e2, N), N)

# Step 2: Set up equations based on C1 and C2
eq1 = Eq(2 * p + 3 * q, C1 % N)
eq2 = Eq(5 * p + 7 * q, C2 % N)

# Step 3: Solve the system of equations
solution = solve((eq1, eq2), (p, q))

# Step 4: Verify and print results
if solution:
    p_value, q_value = solution[p], solution[q]
    if p_value * q_value == N:
        print("Solution found:")
        print("p =", p_value)
        print("q =", q_value)
    else:
        print("No valid solution found that satisfies p * q = N.")
else:
    print("No solution found.")
