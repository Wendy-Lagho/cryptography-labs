state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


# def add_round_key(s, k):
#     return [[s[i][j] ^ k[i][j] for j in range(4)] for i in range(4)]
#
# print(add_round_key(state, round_key))

def add_round_key(s, k):
    """XORs the state matrix with the round key matrix."""
    return [[s[i][j] ^ k[i][j] for j in range(4)] for i in range(4)]

def matrix2bytes(matrix):
    """Converts a 4x4 matrix into a 16-byte array."""
    return bytes(sum(matrix, []))

# Calculate the new state
result_state = add_round_key(state, round_key)

# Convert the resulting state to bytes
result_bytes = matrix2bytes(result_state)

print(result_bytes)
