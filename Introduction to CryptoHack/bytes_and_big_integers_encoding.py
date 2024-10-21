from Crypto.Util.number import *

# Message to convert
message = "HELLO"

# Convert each character to its ASCII byte value
ascii_values = [ord(char) for char in message]
print(f"ASCII values: {ascii_values}")

# Convert each ASCII byte to hexadecimal
hex_values = [hex(ord(char)) for char in message]
print(f"Hexadecimal values: {hex_values}")

# Concatenate the hex values into one large base-16 number (as a string)
# Remove '0x' prefix from each hex value and concatenate them
hex_string = ''.join(format(ord(char), '02x') for char in message)
print(f"Concatenated hex string: 0x{hex_string}")

# Convert the concatenated hex string to a base-10 (decimal) number
decimal_number = int(hex_string, 16)
print(f"Base-10 decimal number: {decimal_number}")

# Code for Converting the Large Integer to a Message
large_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the large base-10 integer back to bytes
message_bytes = long_to_bytes(large_integer)
print(message_bytes)