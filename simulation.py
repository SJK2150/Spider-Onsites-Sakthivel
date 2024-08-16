import random

def encrypt(message, key):
    encrypted_message = ''.join(chr((ord(char) + key) % 256) for char in message)
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ''.join(chr((ord(char) - key) % 256) for char in encrypted_message)
    return decrypted_message

class Node:
    def __init__(self, key):
        self.key = key

    def process(self, message, encrypt_mode=True):
        if encrypt_mode:
            return encrypt(message, self.key)
        else:
            return decrypt(message, self.key)

def simulate_onion_routing(message, nodes):
    encrypted_message = message
    for node in nodes:
        encrypted_message = node.process(encrypted_message, encrypt_mode=True)
        print(f"After node {nodes.index(node)+1} encryption: {encrypted_message}")

    decrypted_message = encrypted_message
    for node in reversed(nodes):
        decrypted_message = node.process(decrypted_message, encrypt_mode=False)
        print(f"After node {nodes.index(node)+1} decryption: {decrypted_message}")

    return decrypted_message

def main():
    nodes = [Node(random.randint(1, 10)) for _ in range(3)]

    original_message = "Please induct me"
    print(f"Original Message: {original_message}")

    final_message = simulate_onion_routing(original_message, nodes)
    print(f"Final Message after Routing: {final_message}")

if __name__ == "__main__":
    main()
