import random
import string

def generate_password(length, level):
    """
    Generate a random password of given length and level.

    Args:
        length (int): Password length.
        level (str): Password level ('easy', 'medium', 'hard').

    Returns:
        str: Generated password.
    """
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    chars = lowercase + uppercase + digits + special_chars

    # Ensure at least one character from each required set is present
    password = []
    password.append(random.choice(lowercase))
    password.append(random.choice(uppercase))
    if level == 'easy':
        password.append(random.choice(lowercase + uppercase))
    elif level == 'medium':
        password.append(random.choice(digits))
    elif level == 'hard':
        password.append(random.choice(special_chars))

    # Fill the rest of the password length with random characters from the chosen set
    for _ in range(length - len(password)):
        password.append(random.choice(chars))

    # Shuffle the password to avoid the first characters always being in the same character set order
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Password Generator")
    print("------------------")
    print("Choose a password level:")
    print("  easy: At least one lowercase and one uppercase letter")
    print("  medium: At least one lowercase, one uppercase letter, and one digit")
    print("  hard: At least one lowercase, one uppercase letter, one digit, and one special character")

    while True:
        level = input("Enter password level (easy, medium, hard): ")
        if level in ['easy', 'medium', 'hard']:
            break
        print("Invalid level. Please choose from 'easy', 'medium', or 'hard'.")

    while True:
        try:
            length = int(input("Enter password length (at least 4): "))
            if length < 4:
                raise ValueError("Password length must be at least 4")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    password = generate_password(length, level)
    print("Generated Password: ", password)

if __name__ == "__main__":
    main()