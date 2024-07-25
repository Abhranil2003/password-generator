import random
import string

def generate_password(length):
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure at least one character from each set is present
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with random characters from all sets
    for _ in range(length - 4):
        password.append(random.choice(lowercase + uppercase + digits + special_chars))

    # Shuffle the password to avoid the first characters always being in the same character set order
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Password Generator")
    print("------------------")
    print("Generated password will contain at least one lowercase letter, one uppercase letter, one digit, and one special character.")

    while True:
        try:
            length = int(input("Enter password length (must be at least 4): "))
            if length < 4:
                raise ValueError("Password length must be at least 4")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    password = generate_password(length)
    print("Generated Password: ", password)

if __name__ == "__main__":
    main()
