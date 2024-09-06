import random
import string

def password_generator(length, use_uppercase, use_numbers, use_special_chars):
    """
    Generates a password of the given length with the specified character types.

    Args:
        length (int): The length of the password.
        use_uppercase (bool): Whether to include uppercase letters.
        use_numbers (bool): Whether to include numbers.
        use_special_chars (bool): Whether to include special characters.

    Returns:
        str: The generated password.
    """
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    password = password_generator(length, use_uppercase, use_numbers, use_special_chars)
    print("Generated Password : ", password)

if __name__ == "__main__":
    main()
