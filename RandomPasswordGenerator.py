import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return f"Generated password: {password}"



if __name__ == '__main__':
    password = generate_password(int(input("Enter the desired password length: ")))

