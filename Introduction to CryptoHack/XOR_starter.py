# Given the string `label`, XOR each character with the integer 13.
# Convert these integers back to a string and submit the flag as crypto{new_string}

def xor_string():

    # Create a list to hold the XORed characters
    xor_result = []
    message = "label"
    for char in message:
        # XOR the ASCII value of the character with the given integer
        xor_char = ord(char) ^ 13
        # Convert the result back to a character and append to the result list
        xor_result.append(chr(xor_char))

    return ''.join(xor_result)

# Call the function
new_string = xor_string()

# Format the result
flag = f"crypto{{{new_string}}}"
print(flag)