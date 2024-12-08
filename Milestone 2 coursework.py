import random
from sympy import isprime, mod_inverse

def generate_keys():
    while True:
        p = random.randint(100, 200)
        if isprime(p):
            break
    g = random.randint(2, p - 1)
    x = random.randint(1, p - 2)
    h = pow(g, x, p)
    return (p, g, h), x

def encrypt(public_key, message):
    p, g, h = public_key
    k = random.randint(1, p - 2)
    c1 = pow(g, k, p)
    c2 = (message * pow(h, k, p)) % p
    return c1, c2

def decrypt(ciphertext, private_key, public_key):
    c1, c2 = ciphertext
    p, _, _ = public_key
    s = pow(c1, private_key, p)
    s_inv = mod_inverse(s, p)
    return (c2 * s_inv) % p


public_key, private_key = generate_keys()
message = 42
ciphertext = encrypt(public_key, message)
decrypted_message = decrypt(ciphertext, private_key, public_key)
print("Public Key:", public_key)
print("Private Key:", private_key)
print("Message:", message)
print("Ciphertext:", ciphertext)
print("Decrypted Message:", decrypted_message)