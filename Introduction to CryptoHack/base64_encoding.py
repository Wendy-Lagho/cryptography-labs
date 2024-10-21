import base64

# this will convert the hexadecimals to bytes
byte_data = bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")

# now to encode this to base64
base64_encoded = base64.b64encode(byte_data)
print(base64_encoded)