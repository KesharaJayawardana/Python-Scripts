# password_generator.py
# Simple secure password generator

import secrets
import string
import argparse

def generate_password(length=16):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a secure password")
    parser.add_argument("-l", "--length", type=int, default=16, help="password length")
    args = parser.parse_args()
    print(generate_password(args.length))
