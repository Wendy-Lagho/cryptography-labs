from pwn import *
from datetime import datetime
from ecdsa.ecdsa import Public_key, Private_key, Signature, generator_192
from Crypto.Util.number import bytes_to_long, long_to_bytes
import json

g = generator_192
n = g.order()

io = remote('socket.cryptohack.org', 13381)
io.recvline()

send_time = dict()
send_time['option'] = 'sign_time'

def send_payload(time):
    while True:
        now = datetime.now()
        if now.strftime("%S") == time:
            io.sendline(json.dumps(send_time).encode())
            return json.loads(io.recvline())
        sleep(1)

def sha1(data):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(data)
    return sha1_hash.digest()

# Send first payload, time we want is 02
signature_1 = send_payload("02")
msg_1 = bytes_to_long(sha1(signature_1['msg'].encode()))

temp = Signature(int(signature_1['r'], 16), int(signature_1['s'], 16))

# There are two possible public keys from the signature observed
public_key_1, public_key_2 = temp.recover_public_keys(msg_1, g)

# Wait for another minute
sleep(1)

# Send next payload, time we want is 03
signature_2 = send_payload("03")
msg_2 = bytes_to_long(sha1(signature_2['msg'].encode()))
r1, s1 = int(signature_1['r'], 16), int(signature_1['s'], 16)
r2, s2 = int(signature_2['r'], 16), int(signature_2['s'], 16)

# Verify if the same nonce is reused
print(r1 == r2)

# Code from https://billatnapier.medium.com/ecdsa-weakness-where-nonces-are-reused-2be63856a01a
inv = pow(r1 * (s1 - s2), -1, n)
secret = ((s2 * msg_1 - s1 * msg_2) * inv) % n

# Two private keys from two possible public keys
privKey_1 = Private_key(public_key_1, secret)
privKey_2 = Private_key(public_key_2, secret)

flag = dict()
flag['option'] = 'verify'
flag['msg'] = "unlock"

# Send the first message with the first public key
hsh = bytes_to_long(sha1("unlock".encode()))
sig = privKey_1.sign(hsh, 42)
flag['r'] = hex(sig.r)
flag['s'] = hex(sig.s)

io.sendline(json.dumps(flag).encode())
print(io.recvline())

# Send the second message with the second public key
sig = privKey_2.sign(hsh, 42)
flag['r'] = hex(sig.r)
flag['s'] = hex(sig.s)

io.sendline(json.dumps(flag).encode())
print(io.recvline())

io.close()