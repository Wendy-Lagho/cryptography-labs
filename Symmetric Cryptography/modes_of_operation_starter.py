import requests

# Replace this with the actual base URL provided by the challenge
BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

# Step 1: Get the encrypted FLAG
def get_encrypted_flag():
    url = f"{BASE_URL}/encrypt_flag/"
    print(f"Requesting URL: {url}")  # Debugging line to ensure URL is correct
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['ciphertext']
    else:
        raise Exception("Failed to get the encrypted FLAG.")

# Step 2: Decrypt the encrypted FLAG
def decrypt_flag(ciphertext):
    url = f"{BASE_URL}/decrypt/{ciphertext}/"
    print(f"Requesting URL: {url}")  # Debugging line to ensure URL is correct
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['plaintext']
    else:
        raise Exception("Failed to decrypt the FLAG.")

# Step 3: Convert hex to ASCII (decrypted flag will be in hex format)
def hex_to_ascii(hex_str):
    return bytes.fromhex(hex_str).decode('utf-8')

# Main function
if __name__ == "__main__":

        # Get the encrypted FLAG
        encrypted_flag = get_encrypted_flag()
        print(f"Encrypted FLAG: {encrypted_flag}")

        # Decrypt the FLAG
        decrypted_hex = decrypt_flag(encrypted_flag)
        print(f"Decrypted FLAG (Hex): {decrypted_hex}")

        # Convert hex to ASCII to get the final FLAG
        flag = hex_to_ascii(decrypted_hex)
        print(f"FLAG: {flag}")
