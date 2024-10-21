def hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string)

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# Given hex strings
KEY1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2_xor_key1_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_xor_key3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_xor_keys_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# Step 1: Decode hex strings to bytes
KEY1 = hex_to_bytes(KEY1_hex)
key2_xor_key1 = hex_to_bytes(key2_xor_key1_hex)
key2_xor_key3 = hex_to_bytes(key2_xor_key3_hex)
flag_xor_keys = hex_to_bytes(flag_xor_keys_hex)

# Step 2: Derive KEY2
KEY2 = xor_bytes(key2_xor_key1, KEY1)

# Step 3: Derive KEY3 using KEY2
KEY3 = xor_bytes(key2_xor_key3, KEY2)

# Step 4: Extract the FLAG using the derived keys
FLAG = xor_bytes(flag_xor_keys, KEY1)
FLAG = xor_bytes(FLAG, KEY3)
FLAG = xor_bytes(FLAG, KEY2)

# Convert FLAG bytes back to a string
print(f"The flag is: {FLAG}")
