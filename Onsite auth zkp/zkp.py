import hashlib
import random

p = 23
g = 5

def registeruser(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    private_key = random.randint(1, p-1)
    public_key = pow(g, private_key, p)
    
    server_database = {
        "hashed_password": hashed_password,
        "public_key": public_key
    }
    
    return private_key, server_database

password = "password"
private_key, server_database = registeruser(password)
print("User registered with public key:", server_database["public_key"])

def generatechallenge():
    return random.randint(1, p-1)

def generateproof(server_database, private_key, challenge):
    k = random.randint(1, p-1)
    r = pow(g, k, p)
    e = hashlib.sha256((str(r) + str(challenge)).encode()).hexdigest()
    e = int(e, 16) % p
    s = (k + e * private_key) % (p-1)
    return r, e, s

def verifyproof(server_database, r, e, s, challenge):
    r_prime = (pow(g, s, p) * pow(server_database["public_key"], e, p)) % p
    e_prime = hashlib.sha256((str(r_prime) + str(challenge)).encode()).hexdigest()
    e_prime = int(e_prime, 16) % p
    return e == e_prime

challenge = generatechallenge()
r, e, s = generateproof(server_database, private_key, challenge)
if verifyproof(server_database, r, e, s, challenge):
    print("User successfully authenticated!")
else:
    print("Authentication failed.")
